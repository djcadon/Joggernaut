import streamlit as st
from db_queries.user import new_user
from db_queries.user_metrics import get_user_metrics
from db_queries.goals import user_goals
import datetime

# Initialize session state to store user info
if 'user_details' not in st.session_state:
    st.session_state.user_details = {'id': 0, 'name': '', 'height': '', 'weight': '', 'age': 0}

# Function to handle user sign-up logic
def user_signup(username, password, dob, height, weight, goal_weight):
    lg = new_user(username, password, dob, height, weight, goal_weight)
    if lg[0] == 'Success':
        # Save user ID and name in session
        st.session_state.user_details['id'] = lg[1]
        st.session_state.user_details['name'] = username

        # Fetch and store height, weight, and goal
        user_info = get_user_metrics(lg[1])
        st.session_state.user_details['height'] = user_info.get('height')
        st.session_state.user_details['weight'] = user_info.get('weight')
        st.session_state.user_details['goal_weight'] = goal_weight

        return True
    else:
        return False

# Set up the Streamlit page
st.set_page_config(page_title='Signup', layout='centered', initial_sidebar_state='collapsed')
st.title('Sign Up')

# Hide sidebar using HTML/CSS
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

# Page heading
st.title("🔐 Sign Up Page")

# Hide Streamlit menu and footer
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Button to switch to login page
existing_account = st.button('Already Have an Account')

# Form for user sign-up
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    dob = st.date_input("Date of Birth", min_value=datetime.date.min)
    height = st.text_input("Height (cm)")
    weight = st.text_input("Weight (kg)")
    goal_weight = st.text_input("Goal Weight (kg)")
    submitted = st.form_submit_button("Sign Up")

    # Redirect if already has an account
    if existing_account:
        st.switch_page('./login.py')

    # Handle form submission
    if submitted:
        sub_height = float(height)
        sub_weight = float(weight)
        sub_goal_weight = float(goal_weight)

        if user_signup(username, password, dob, sub_height, sub_weight, sub_goal_weight):
            st.success(f"Welcome, {username}!")
            st.balloons()
            st.session_state['logged_in'] = True
        else:
            st.error("Invalid username or password")

# Redirect to home if logged in
if st.session_state.get('logged_in'):
    st.switch_page('pages/Home.py')
