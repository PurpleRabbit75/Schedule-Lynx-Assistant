import streamlit as st

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