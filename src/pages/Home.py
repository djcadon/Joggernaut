import streamlit as st
from db_config import connect_db

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')


st.title('Joggernaut')

st.text('Welcome to Joggernaut!')

# Example improt

# cur, conn = connect_db()
# cur.close()
# conn.close()