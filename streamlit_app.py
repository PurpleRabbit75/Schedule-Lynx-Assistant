import streamlit as st
# import json

# if ("config" not in st.session_state):
#     with open('config/config.json', 'r') as file:
#         st.session_state['config'] = json.load(file)
if ("data" not in st.session_state):
    st.session_state['data'] = []


pages = {
    '': [
    st.Page("generator.py", title="Create Schedule Files"),
    st.Page("help.py", title="Help")
    ]
}

pg = st.navigation(pages)
pg.run()