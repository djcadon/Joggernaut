# Import necessary modules and functions
import streamlit as st
from db_queries.user import login
from db_queries.user_metrics import get_user_metrics
from db_queries.goals import user_goals

# Initialize user session details if not already present
if 'user_details' not in st.session_state:
    st.session_state.user_details = {'id': 0, 'name': '', 'height':'', 'weight': '', 'age': 0}

# Function to log in a user
def user_login(username, password):
    lg = login(username, password)
    if lg[0] == 'Success':
        # Store user ID and name
        st.session_state.user_details['id'] = lg[1]
        st.session_state.user_details['name'] = username

        # Fetch and store user metrics
        user_info = get_user_metrics(lg[1])
        goal_weight = user_goals(lg[1])
        st.session_state.user_details['height'] = user_info.get('height')
        st.session_state.user_details['weight'] = user_info.get('weight')
        st.session_state.user_details['goal_weight'] = goal_weight

        return True
    else:
        return False

# Streamlit page setup
st.set_page_config(page_title='Login', layout='centered', initial_sidebar_state='collapsed')
st.title('Login')

# Hide sidebar
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

# Title on the page
st.title("🔐 Login Page")

# Initialize login state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Hide main menu and footer for a clean look
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Login form UI
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Submit buttons: Login and Sign Up
    col1, col2, _, _, _, _, _= st.columns(7)
    with col1:
        submitted = st.form_submit_button("Login")
    with col2:
        signup = st.form_submit_button('Sign Up')

    # Handle login action
    if submitted:
        if user_login(username, password):
            st.success(f"Welcome, {username}!")
            st.balloons()
            st.session_state['logged_in'] = True
        else:
            st.error("Invalid username or password")

    # Redirect to sign-up page if selected
    if signup:
        st.switch_page('pages/signup.py')

# If user successfully logged in, go to Home page
if st.session_state.get('logged_in'):
    st.switch_page('pages/Home.py')
