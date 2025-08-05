import streamlit as st
from db_queries.exercises import get_exercise_by_user, edit_exercise, delete_exercise, new_exercise


st.set_page_config(layout='wide')

st.title('Your Exercises')


if st.session_state.get('logged_in'):
    uid = st.session_state.user_details['id']
    exercises = get_exercise_by_user(uid)

    if isinstance(exercises, str):  # Catch error string
        st.error(exercises)
    else:

       
        # ---- INIT SESSION FLAGS ----
        if 'edit_mode' not in st.session_state:
            st.session_state.edit_mode = {}
        if 'adding_new' not in st.session_state:
            st.session_state.adding_new = False


        # Add New Exercise
        if not st.session_state.adding_new:
            if st.button("➕ Add Exercise"):
                st.session_state.adding_new = True
                st.rerun()
        else:
            with st.form("new_exercise_form", clear_on_submit=True):
                st.subheader("Add a New Exercise")
                new_name = st.text_input("Name")
                new_desc = st.text_area("Description")
                submitted = st.form_submit_button("Submit")
                cancel = st.form_submit_button("Cancel")

                if submitted:
                    result = new_exercise(uid, new_name, new_desc)
                    st.success(result)
                    st.session_state.adding_new = False
                    st.rerun()
                elif cancel:
                    st.session_state.adding_new = False
                    st.rerun()
                    
        # Column headers
        header_col1, header_col2, header_col3 = st.columns([2, 4, 3])
        with header_col1:
            st.markdown('<p style="margin: 0;"><b>Name</b></p>', unsafe_allow_html=True)
        with header_col2:
            st.markdown('<p style="margin: 0;"><b>Description</b></p>', unsafe_allow_html=True)
        with header_col3:
            st.markdown('<p style="margin: 0;"><b>Actions</b></p>', unsafe_allow_html=True)
            
        st.markdown('<hr style="margin-top: 0;">', unsafe_allow_html=True)  # Divider

        

        # Display the Exersies
        for exercise in exercises:
            ex_id = exercise.get('id')

            if ex_id not in st.session_state.edit_mode:
                st.session_state.edit_mode[ex_id] = False

            with st.container():
                col1, col2, col3 = st.columns([2, 4, 3])

                if st.session_state.edit_mode[ex_id]:
                    # Edit Mode UI
                    new_name = col1.text_input("Name", value=exercise.get('name'), key=f"name_{ex_id}")
                    new_desc = col2.text_area("Description", value=exercise.get('description'), key=f"desc_{ex_id}")

                    if col3.button("Save", key=f"save_{ex_id}"):
                        result = edit_exercise(ex_id, new_name, new_desc)
                        st.success(f"Updated: {result}")
                        st.session_state.edit_mode[ex_id] = False
                        st.rerun()

                    if col3.button("Cancel", key=f"cancel_{ex_id}"):
                        st.session_state.edit_mode[ex_id] = False
                        st.rerun()
                else:
                    # Normal Display Mode
                    col1.write(f"**{exercise.get('name')}**")
                    col2.write(exercise.get('description'))

                    if col3.button("Edit", key=f"edit_{ex_id}"):
                        st.session_state.edit_mode[ex_id] = True
                        st.rerun()

                    if col3.button("Delete", key=f"delete_{ex_id}"):
                        result = delete_exercise(ex_id)
                        st.success(f"Deleted: {result}")
                        st.rerun()
                        
else:
    st.markdown('### Please log in first.')