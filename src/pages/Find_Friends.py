import streamlit as st
from db_queries.user import search_user
from db_queries.friends import new_friend_connection

if 'logged_in' in st.session_state:
    st.title('Find Friends')

    name = st.text_input('Enter Username')

    results = search_user(name)

    if results:
        for result in results:
            col1, col2, col3 = st.columns([2, 2, 1])

            with col1:
                st.write(result.get('name'))

            with col2:
                st.write(result.get('dob'))

            with col3:
                # Unique button key to avoid conflicts
                if st.button('Add Friend', key=f"add_{result.get('id')}"):
                    success = new_friend_connection(
                        st.session_state.user_details['id'],
                        result.get('id')
                    )
                    if success:
                        st.success(f"Friend request sent to {result.get('name')}")
                    else:
                        st.error("Failed to add friend. Maybe you're already connected?")
    else:
        st.write("No users found.")
else:
    st.write('### Please log in to continue')
