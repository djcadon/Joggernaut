import streamlit as st

st.set_page_config(layout='centered')
st.title('User Profile')

# We will later convert this to a db query and session state thing
user_name = 'Joe'
current_weight = '80 KG'
current_height = '170cm'
goal_weight = '75 KG'

if st.session_state.logged_in == True:
    # Define CSS style
    st.markdown("""
        <style>
        .profile-section {
            background-color: #f9f9f9;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 20px;
            font-family: Arial, sans-serif;
            width: 100%;
            max-width: 400px;
        }
        .profile-section h2 {
            font-size: 18px;
            color: #333333;
            margin-top: 0;
        }
        .profile-section .profile-item {
            margin-bottom: 15px;
            font-size: 16px;
            color: #555555;
        }
        .profile-section .profile-item label {
            font-weight: bold;
            color: #888888;
        }
        .profile-section .profile-item a {
            color: #ff6f61;
            text-decoration: none;
        }
        .profile-section .profile-item a:hover {
            text-decoration: underline;
        }
        </style>
        """, unsafe_allow_html=True)

    # Display profile information using HTML
    st.markdown(f"""
    <div class="profile-section">
        <h2>Personal Information</h2>
        <div class="profile-item">
            <label>Name:</label> {user_name}
        </div>
        <div class="profile-item">
            <label>Current Weight:</label> {current_weight}
        </div>
        <div class="profile-item">
            <label>Current Height:</label> {current_height}
        </div>
        <div class="profile-item">
            <label>Goal Weight:</label> {goal_weight}
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown('### Please login to continue')