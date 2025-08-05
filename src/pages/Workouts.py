import streamlit as st
import time
from datetime import timedelta

from db_queries.workouts import get_workouts_by_user, new_workout, edit_workout, delete_workout
from db_queries.exercises import get_exercise, get_exercise_by_user, get_all_exercises
from db_queries.progress import new_progress_entry, edit_progress_entry, delete_progress_entry, get_progress_by_exercise
from db_queries.exercises_workouts import  add_exercise_to_workout, remove_exercise_from_workout, update_exercise_in_workout, get_exercises_by_workout

st.title('💪 My Workouts')

if 'logged_in' in st.session_state:

    #INITIALIZE SESSION STATE VARIABLES
    if 'workout_timer' not in st.session_state:
        st.session_state['workout_timer'] = {}

    if 'adding_workout' not in st.session_state:
        st.session_state['adding_workout'] = False


    # Adding workout
    if st.button("➕ Add Workout"):
        st.session_state['adding_workout'] = True

    if st.session_state['adding_workout']:
        all_exercises = get_exercise_by_user(st.session_state.user_details['id'])  # List of dicts with exercise data
        exercise_names = [f"{e['name']} " for e in all_exercises]
        exercise_id_lookup = {f"{e['name']} ": e['id'] for e in all_exercises}

        with st.form("new_workout_form", clear_on_submit=True):
            name = st.text_input("Workout Name")
            day = st.selectbox("Day of the Week", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
            selected_exercises = st.multiselect("Select Exercises", options=exercise_names)
            submitted = st.form_submit_button("Create Workout")

            if submitted:
                workout = new_workout(st.session_state.user_details['id'], name, day)
                workout_id = workout['id']  

                # Link each selected exercise to the workout
                for selected in selected_exercises:
                    eid = exercise_id_lookup[selected]
                    print(add_exercise_to_workout(eid=eid, wid=workout_id))

                st.success("Workout with exercises added.")
                st.session_state['adding_workout'] = False
                st.rerun()



# Displaying workouts

    workouts = get_workouts_by_user(st.session_state.user_details['id'])

    for workout in workouts:
        wid = workout.get('id')
        exercises = get_exercises_by_workout(wid)

        with st.expander(f"{workout.get('name')} -> {workout.get('days_of_week')}", expanded=False):
            col1, col2 = st.columns([8, .5])
            
            with col2:
                # Delete Workout Button
                
                if st.button(f"🗑️", key=f"delete_{wid}"):
                    result = delete_workout(wid)
                    if result == "Success":
                        st.success("Workout deleted successfully.")
                        st.rerun()
                    else:
                            st.error(f"Error deleting workout: {result}")
                
            with col1:
                st.write("### Exercises")
                for exercise in exercises:
                    st.write(f"- {exercise.get('name')}: {exercise.get('description')}")


            # Start/Stop Button Logic
            if wid not in st.session_state['workout_timer']:
                st.session_state['workout_timer'][wid] = {"started": False, "start_time": None}

            col1, col2 = st.columns(2)
            
            def format_duration(seconds):
                return str(timedelta(seconds=int(seconds)))
            
            with col1:
                if not st.session_state['workout_timer'][wid]["started"]:
                    if st.button(f"▶️ Start Workout", key=f"start_{wid}"):

                        st.session_state['workout_timer'][wid]["started"] = True
                        st.session_state['workout_timer'][wid]["start_time"] = st.session_state.get("timer_now", time.time())

                        
                        st.rerun()
                else:
                    start_time = st.session_state['workout_timer'][wid]["start_time"]
                    elapsed = time.time() - start_time
                    st.markdown(f"⏱️ **Elapsed Time:** {format_duration(elapsed)}")
                    time.sleep(1) 
                     

            with col2:
                if st.session_state['workout_timer'][wid]["started"]:
                    
                    
                    if st.button(f"⏹️ Stop Workout", key=f"stop_{wid}"):
                        
                        
                        start = st.session_state['workout_timer'][wid]["start_time"]
                        end = time.time()
                        duration = round(end - start, 2)  # in seconds

                        # Save to progress DB for each exercise
                        for exercise in exercises:
                            uid = st.session_state.user_details.get('id')
                            eid = exercise.get('id')
                            duration = round(duration / 60, 2)

                            st.write(f"⏳ Inserting progress for Exercise ID: `{eid}`, Duration: `{duration}` mins")

                            try:
                                result = new_progress_entry(
                                    uid=uid,
                                    eid=eid,
                                    wid=wid,
                                    weight=0,  # Optional, adjust if needed
                                    duration_mins=duration
                                )
                                st.success(f"✅ Progress inserted for Exercise ID: `{eid}`")

                                # Optional: show returned result if your function returns something
                                st.write(f"🗒️ Result: {result}")

                            except Exception as e:
                                st.error(f"❌ Failed to insert progress for Exercise ID `{eid}`")
                                st.exception(e)

                        st.session_state['workout_timer'][wid] = {"started": False, "start_time": None}
                        st.success(f"Workout Duration: {round(duration)} mins recorded for all exercises.")
                        time.sleep(2) 
                        st.rerun()
                else:
                    # Timer Tick rate
                    time.sleep(1)
                    st.rerun()
                        

else:
    st.write('### Please log in to continue')