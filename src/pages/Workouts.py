import streamlit as st
import time
from datetime import timedelta

from db_queries.workouts import get_workouts_by_user, new_workout, edit_workout, delete_workout
from db_queries.exercises import get_exercise_by_user
from db_queries.progress import new_progress_entry
from db_queries.exercises_workouts import (
    add_exercise_to_workout,
    get_exercises_by_workout
)

st.title('💪 My Workouts')

# Make sure user is logged in
if 'logged_in' not in st.session_state:
    st.write('### Please log in to continue')
    st.stop()

# Initialize state for adding workout and workout timers
if 'adding_workout' not in st.session_state:
    st.session_state['adding_workout'] = False

if 'workout_timer' not in st.session_state:
    st.session_state['workout_timer'] = {}

# Helper to convert seconds to HH:MM:SS
def format_duration(seconds):
    return str(timedelta(seconds=int(seconds)))

# Add workout form
if st.button("➕ Add Workout"):
    st.session_state['adding_workout'] = True

if st.session_state['adding_workout']:
    # Get all exercises for this user
    all_exercises = get_exercise_by_user(st.session_state.user_details['id'])
    exercise_names = [e['name'] for e in all_exercises]
    exercise_id_lookup = {e['name']: e['id'] for e in all_exercises}

    # New workout form
    with st.form("new_workout_form", clear_on_submit=True):
        name = st.text_input("Workout Name")
        day = st.selectbox("Day of the Week", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
        selected_exercises = st.multiselect("Select Exercises", options=exercise_names)
        submitted = st.form_submit_button("Create Workout")

        if submitted:
            # Save workout and link exercises
            workout = new_workout(st.session_state.user_details['id'], name, day)
            workout_id = workout['id']

            for selected in selected_exercises:
                eid = exercise_id_lookup[selected]
                add_exercise_to_workout(eid=eid, wid=workout_id)

            st.success("Workout with exercises added.")
            st.session_state['adding_workout'] = False
            st.rerun()

# Load all workouts for user
workouts = get_workouts_by_user(st.session_state.user_details['id'])

# Display each workout
for workout in workouts:
    wid = workout['id']
    workout_name = workout['name']
    workout_day = workout['days_of_week']
    exercises = get_exercises_by_workout(wid)

    # Setup timer for this workout
    if wid not in st.session_state['workout_timer']:
        st.session_state['workout_timer'][wid] = {"started": False, "start_time": None}

    with st.expander(f"{workout_name} → {workout_day}", expanded=False):

        # Delete workout button
        delete_col, main_col = st.columns([1, 8])
        with delete_col:
            if st.button("🗑️", key=f"delete_{wid}"):
                result = delete_workout(wid)
                if result == "Success":
                    st.success("Workout deleted.")
                    st.rerun()
                else:
                    st.error(f"Failed to delete workout: {result}")

        # Show exercises inside workout
        with main_col:
            st.write("### Exercises")
            for exercise in exercises:
                eid = exercise['id']
                ename = exercise['name']

                # Unique key for storing weight input
                weight_key = f"weight_input_{wid}_{eid}"

                # Set default weight if not already in session state
                if weight_key not in st.session_state:
                    st.session_state[weight_key] = 0.0

                st.write(f"**{ename}** - {exercise['description']}")
                st.number_input(
                    f"Enter weight used (kg) for {ename}",
                    min_value=0.0,
                    step=2.5,
                    key=weight_key
                )

            # Show timer status
            timer = st.session_state['workout_timer'][wid]
            now = time.time()

            if timer["started"]:
                elapsed = now - timer["start_time"]
                st.success(f"⏱️ Workout Started! Elapsed: {format_duration(elapsed)}")
            else:
                st.info("Workout not started yet.")

            # Timer buttons: Start & Stop
            start_col, stop_col = st.columns(2)

            with start_col:
                if not timer["started"]:
                    if st.button("▶️ Start", key=f"start_{wid}"):
                        st.session_state['workout_timer'][wid] = {
                            "started": True,
                            "start_time": now
                        }
                        st.rerun()

            with stop_col:
                if timer["started"]:
                    if st.button("⏹️ Stop", key=f"stop_{wid}"):
                        start = timer["start_time"]
                        duration_secs = now - start
                        duration_mins = round(duration_secs / 60, 2)

                        uid = st.session_state.user_details['id']
                        # Save progress for each exercise
                        for exercise in exercises:
                            eid = exercise['id']
                            ename = exercise['name']
                            weight_key = f"weight_input_{wid}_{eid}"
                            weight = st.session_state.get(weight_key, 0.0)

                            try:
                                result = new_progress_entry(
                                    uid=uid,
                                    eid=eid,
                                    wid=wid,
                                    weight=weight,
                                    duration_mins=duration_mins
                                )
                                st.success(f"✅ Progress saved for {ename} ({duration_mins} mins, {weight} kg)")
                            except Exception as e:
                                st.error(f"❌ Error saving progress for {ename}")
                                st.exception(e)

                        # Reset timer
                        st.session_state['workout_timer'][wid] = {"started": False, "start_time": None}
                        st.rerun()
