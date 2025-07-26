import streamlit as st
from db_queries.friends import get_all_friends

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')


st.title('Joggernaut')

st.text('Welcome to Joggernaut!')

st.markdown(f'''
            ##### See what your friends are up to!
            ''', unsafe_allow_html=True)

friend_deets = get_all_friends(st.session_state.user_details.get('id'))
for i in friend_deets:
    st.write(i)