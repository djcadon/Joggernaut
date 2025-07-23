import streamlit as st
from db_config import connect_db

st.set_page_config(layout='wide')
st.title('Joggernaut')

st.text('More stuff here')

# Example improt

# cur, conn = connect_db()
# cur.close()
# conn.close()