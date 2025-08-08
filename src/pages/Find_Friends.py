import streamlit as st
from db_queries.user import search_user
from db_queries.friends import new_friend_connection

# Check if user is logged in
if 'logged_in' in st.session_state:
    st.title('Find Friends')

    # Input field to search for a username
    name = st.text_input('Enter Username')

    # Get search results based on the input name
    results = search_user(name)

    # If results are found, display them
    if results:
        for result in results:
            # Create 3 columns to layout the name, DOB, and button
            col1, col2, col3 = st.columns([2, 2, 1])

            with col1:
                st.write(result.get('name'))  # Show the user's name

            with col2:
                st.write(result.get('dob'))  # Show the user's DOB

            with col3:
                # Button to add friend, uses unique key per user to avoid duplicates
                if st.button('Add Friend', key=f"add_{result.get('id')}"):
                    # Try to create a new friend connection
                    success = new_friend_connection(
                        st.session_state.user_details['id'],
                        result.get('id')
                    )
                    # Show success or error message based on result
                    if success:
                        st.success(f"Friend request sent to {result.get('name')}")
                    else:
                        st.error("Failed to add friend. Maybe you're already connected?")
    else:
        # If no users matched the search
        st.write("No users found.")
else:
    # Prompt user to log in
    st.write('### Please log in to continue')
