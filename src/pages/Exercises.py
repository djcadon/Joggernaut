import streamlit as st
from db_queries.exercises import get_exercise_by_user

st.set_page_config(layout='wide')

st.title('Your exercises')

if st.session_state.logged_in == True:
    exercises = get_exercise_by_user(st.session_state.user_details['id'])

    col1, col2 = st.columns([1,4])
    with col1:
        st.write('Name')

    with col2:
        col2.write('Description')

    for exercise in exercises:
        with col1:
            st.write(exercise.get('name'))

        with col2:
            st.write(exercise.get('description'))
else:
    st.markdown('### Please log in first.')