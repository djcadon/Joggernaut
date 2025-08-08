import streamlit as st
from db_queries.progress import get_progress_by_exercise, get_all_progress_records
from db_queries.exercises import get_exercise_by_user
from utils.time_converter import consolidate_time
from datetime import datetime

# Title of the page
st.title('📈 My Progress')

# If the user is not logged in, show message and stop the app
if 'logged_in' not in st.session_state:
    st.write('### Please log in to continue')
    st.stop()

# Get the logged-in user's ID
uid = st.session_state.user_details['id']

# Section to show all progress records
st.header("🗂️ All Progress Records")

# Get all progress data for the user
all_prog = get_all_progress_records(uid)

# Rename column keys and format time
for element in all_prog:
    element['Exercise Name'] = element.pop('ex_name')
    element['Workout Name'] = element.pop('w_name')
    element['Weight'] = element.pop('weight')
    element['Time Taken'] = consolidate_time(element.pop('duration_mins'))

# Show results in a table if data exists
if all_prog:
    st.dataframe(all_prog, use_container_width=True)
else:
    st.info("No progress records found.")

# Section to show progress by specific exercise
st.header("🏋️ Progress by Exercise")

# Add a toggle/checkbox to show or hide this section
toggle = st.checkbox("Show Progress by My Exercises", value=False)

# If the checkbox is checked
if toggle:
    # Get all exercises created by this user
    exercises = get_exercise_by_user(uid)

    # If user has exercises
    if exercises:
        for ex in exercises:
            eid = ex['id']  # Exercise ID
            ename = ex['name']  # Exercise Name

            # Get progress entries for this specific exercise
            progress = get_progress_by_exercise(uid=uid, eid=eid)

            # Format timestamps to readable strings
            for element in progress:
                date_str = "2025-08-06 20:16:14+00:00"
                dt = datetime.fromisoformat(date_str)
                formatted = dt.strftime("%Y-%m-%d %H:%M:%S")
                element['created_at'] = formatted

            # Rename keys and format duration
            for element in progress:
                element['Exercise Name'] = element.pop('ex_name')
                element['Workout Name'] = element.pop('w_name')
                element['Weight'] = element.pop('weight')
                element['Time Taken'] = consolidate_time(element.pop('duration_mins'))
                element['Time of Progress'] = element.pop('created_at')

            # Create expandable section for each exercise
            with st.expander(f"{ename}", expanded=False):
                if progress:
                    st.table(progress)  # Show progress in a table
                else:
                    st.info("No progress found for this exercise.")
    else:
        st.warning("You don't have any exercises yet.")
