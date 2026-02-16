import streamlit as st
import json

# if ("config" not in st.session_state):
#     with open('config/config.json', 'r') as file:
#         st.session_state['config'] = json.load(file)
# if ("colors" not in st.session_state):
#     with open('config/colors.json', 'r') as file:
#         st.session_state['colors'] = [tuple(color) for color in list(json.load(file).values())]


pages = {
    '': [
    st.Page("generator.py", title="Create Schedule Files"),
    st.Page("help.py", title="Help")
    ]
   
    # "Main App": [
    #     st.Page("GUI/upload.py", title="Upload Files"),
    #     st.Page("GUI/review.py", title="Review Uploads"),
    #     st.Page("GUI/download.py", title="Download Schedule"),
    # ],
    # "Settings": [
    #     st.Page("GUI/config.py", title="Configuration"),
    #     st.Page("GUI/colors.py", title="Colors"),
    # ],
}

pg = st.navigation(pages)
pg.run()