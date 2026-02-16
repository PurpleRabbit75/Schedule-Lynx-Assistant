import streamlit as st
import json
from io import StringIO
import time

days_mapping = {"Monday" : "M", "Tuesday" : "T", "Wednesday" : "W", "Thursday" : "R", "Friday" : "F"}
data = []

name = st.text_input("Name:")
data.append(name)

st.divider()

def add_entry():
    keyStr = str(time.time())
    with st.container():
        entry = []
        col1, col2, col3 = st.columns(3)
        with col1:
            start_time = st.time_input("Start Time:", value = None, key = keyStr + "_start")
            if start_time is not None:
                entry.append([start_time.hour, start_time.minute])
        with col2:
            end_time = st.time_input("End Time:", value = None, key = keyStr + "_end")
            if end_time is not None:
                entry.append([end_time.hour, end_time.minute])
        with col3:
            days = st.multiselect("Days of the Week:", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], key = keyStr + "_days")
            entry.append(''.join([days_mapping[day] for day in days]))
        data.append(entry)
    


add_entry()
st.divider()
add_entry()




json_buffer = StringIO()
json.dump(data, json_buffer)
json_content = json_buffer.getvalue()
st.divider()
st.download_button('Download', json_content, file_name=f"{name}.json", mime='application/json')

