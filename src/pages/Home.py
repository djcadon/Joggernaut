import streamlit as st
from db_queries.friends import get_all_friends

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')


st.title('Joggernaut')

st.text('Welcome to Joggernaut!')

st.markdown(f'''
            ##### See what your friends are up to!
            ''', unsafe_allow_html=True)

friend_deets = get_all_friends(st.session_state.user_details.get('id'))

col1, col2, col3 = st.columns(3)

with col1:
    st.write('Name')

with col2:
    st.write('Weight')

with col3:
    st.write('Height')

for friend in friend_deets:
    with col1:
        st.write(friend.get('name'))

    with col2:
        st.write(str(f"{friend.get('weight')} KG"))

    with col3:
        st.write(str(f"{friend.get('height')} CM"))
