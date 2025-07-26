import streamlit as st
from db_queries.user import new_user
from db_queries.user_metrics import get_user_metrics
import datetime

if 'user_details' not in st.session_state:
    st.session_state.user_details = {'id': 0, 'name': '', 'height':'', 'weight': '', 'age': 0}

# Again, placeholder for testing
def user_signup(username, password, dob, height, weight):
    lg = new_user(username, password, dob, height, weight)
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
st.set_page_config(page_title='Signup', layout='centered', initial_sidebar_state='collapsed')
st.title('Sign Up')

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

st.title("🔐 Sign Up Page")

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
    dob = st.date_input("Date of Birth", min_value=datetime.date.min)
    height = st.text_input("Height (cm)")
    weight = st.text_input("Weight (kg)")
    goal_weight = st.text_input("Goal Weight (kg)")
    submitted = st.form_submit_button("Sign Up")



    if submitted:
        sub_height = float(height)
        sub_weight = float(weight)
        sub_goal_weight = float(goal_weight)
        if new_user(username, password, dob, height, weight, goal_weight):
            st.success(f"Welcome, {username}!")
            st.balloons()
            st.session_state['logged_in'] = True
        else:
            st.error("Invalid username or password")

# Example protected content
if st.session_state.get('logged_in'):
    st.switch_page('pages/Home.py')