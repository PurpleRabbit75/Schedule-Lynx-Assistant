import streamlit as st

with open('extras/help.md', 'r') as file:
    st.markdown(file.read(), unsafe_allow_html=True)

st.caption("""Privacy Policy: We do not collect or store any information in way way whatsoever. 
We never have and we never will.""")