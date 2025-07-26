import streamlit as st
from db_queries.user import login
from db_queries.user_metrics import get_user_metrics
from db_config import connect_db

# This is just a placeholder for now, we'll make a real one
USER_CREDENTIALS = {
    "admin": "admin123",
    "user1": "pass1",
    "user2": "pass2"
}

if 'user_details' not in st.session_state:
    st.session_state.user_details = {'id': 0, 'name': '', 'height':'', 'weight': '', 'age': 0}

# Again, placeholder for testing
def user_login(username, password):
    lg = login(username, password)
    print(lg)
    if lg[0] == 'Success':
        st.session_state.user_details['id'] = lg[1]
        st.session_state.user_details['name'] = username

        user_info = get_user_metrics(lg[1])
        st.session_state.user_details['height'] = user_info.get('height')
        st.session_state.user_details['weight'] = user_info.get('weight')

        return True
    else:
        return False

# Streamlit stuff (This can stay, most of it)
st.set_page_config(page_title='Login', layout='centered', initial_sidebar_state='collapsed')
st.title('Login')

st.markdown(
    """
<style>
    [data-testid="stSidebar"] {
        display: none
    }

</style>
""",
    unsafe_allow_html=True,
)

st.title("🔐 Login Page")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Hide menu and footer
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        if user_login(username, password):
            st.success(f"Welcome, {username}!")
            st.balloons()
            st.session_state['logged_in'] = True
        else:
            st.error("Invalid username or password")

# Example protected content
if st.session_state.get('logged_in'):
    st.switch_page('pages/Home.py')