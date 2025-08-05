import streamlit as st
from db_queries.progress import get_progress_by_exercise

st.title('My Progress')





if 'logged_in' in st.session_state:
    pass

else:
    st.write('### Please log in to continue')