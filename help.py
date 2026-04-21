import streamlit as st

with open('README.md', 'r') as file:
    st.markdown(file.read(), unsafe_allow_html=True)