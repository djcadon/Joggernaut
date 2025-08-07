import streamlit as st
from db_queries.progress import get_progress_by_exercise, get_all_progress_records
from db_queries.exercises import get_exercise_by_user
from utils.time_converter import consolidate_time
from datetime import datetime

st.title('📈 My Progress')

if 'logged_in' not in st.session_state:
    st.write('### Please log in to continue')
    st.stop()

uid = st.session_state.user_details['id']

st.header("🗂️ All Progress Records")

all_prog = get_all_progress_records(uid)

for element in all_prog:
    element['Exercise Name'] = element.pop('ex_name')
    element['Workout Name'] = element.pop('w_name')
    element['Weight'] = element.pop('weight')
    element['Time Taken'] = consolidate_time(element.pop('duration_mins'))

if all_prog:
    st.dataframe(all_prog, use_container_width=True)
else:
    st.info("No progress records found.")

st.header("🏋️ Progress by Exercise")

toggle = st.checkbox("Show Progress by My Exercises", value=False)

if toggle:
    exercises = get_exercise_by_user(uid)

    if exercises:
        for ex in exercises:
            eid = ex['id']
            ename = ex['name']

            progress = get_progress_by_exercise(uid=uid, eid=eid)

            for element in progress:
                date_str = "2025-08-06 20:16:14+00:00"
                dt = datetime.fromisoformat(date_str)
                formatted = dt.strftime("%Y-%m-%d %H:%M:%S")

                element['created_at'] = formatted

            for element in progress:
                element['Exercise Name'] = element.pop('ex_name')
                element['Workout Name'] = element.pop('w_name')
                element['Weight'] = element.pop('weight')
                element['Time Taken'] = consolidate_time(element.pop('duration_mins'))
                element['Time of Progress'] = element.pop('created_at')

            with st.expander(f"{ename}", expanded=False):
                if progress:
                    st.table(progress)
                else:
                    st.info("No progress found for this exercise.")
    else:
        st.warning("You don't have any exercises yet.")
