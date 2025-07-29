import streamlit as st
from db_queries.workouts import get_workouts_by_user
from db_queries.exercises import get_exercises_by_workout


st.title('My Workouts')

if 'logged_in' in st.session_state:
    workouts = get_workouts_by_user(st.session_state.user_details['id'])

    for workout in workouts:
        exercises =get_exercises_by_workout(workout.get('id'))
        with st.expander(f'{workout.get('name')} -> {workout.get('days_of_week')}', expanded=False, key=f'{workout.get('id')}'):
            for exercise in exercises:
                st.write(f"{exercise.get('name')}: {exercise.get('description')}")

else:
    st.write('### Please log in to continue')