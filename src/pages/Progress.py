import streamlit as st
from db_queries.progress import get_progress_by_exercise, get_all_progress_records
from db_queries.exercises import get_exercise_by_user

st.title('📈 My Progress')

if 'logged_in' not in st.session_state:
    st.write('### Please log in to continue')
    st.stop()

uid = st.session_state.user_details['id']

st.header("🗂️ All Progress Records")

all_prog = get_all_progress_records(uid)

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

            with st.expander(f"{ename}", expanded=False):
                if progress:
                    st.table(progress)
                else:
                    st.info("No progress found for this exercise.")
    else:
        st.warning("You don't have any exercises yet.")
