import streamlit as st
import json
from io import StringIO
from datetime import time


days_mapping = {"Monday" : "M", "Tuesday" : "T", "Wednesday" : "W", "Thursday" : "R", "Friday" : "F"}

# Initialize session state variables that track form state
if 'name_initialized' not in st.session_state:
    st.session_state['name_initialized'] = False
if 'current_name' not in st.session_state:
    st.session_state['current_name'] = ""

name = st.text_input("Name:")

# Only update if name has actually changed
if name != st.session_state['current_name']:
    st.session_state['current_name'] = name
    # Only add non-empty names to data
    if name and name not in st.session_state['data']:
        st.session_state['data'] = [name] + st.session_state['data']

if 'num_entries' not in st.session_state:
    st.session_state['num_entries'] = 1

st.session_state['num_entries'] = st.number_input("Number of Entries", min_value=1, max_value=None, value=st.session_state['num_entries'])

st.divider()



def add_entry(keyStr:str):
    with st.form(key = keyStr + "_form"):
        # entry = []
        col1, col2, col3 = st.columns(3)
        with col1:
            start_time = st.time_input("Start Time:", value = None, key = keyStr + "_start")
        with col2:
            end_time = st.time_input("End Time:", value = None, key = keyStr + "_end")
        with col3:
            days = st.multiselect("Days of the Week:", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], key = keyStr + "_days")

        
        submitted = st.form_submit_button("Save")
        if submitted:
            # Build entry from form values
            entry = []
            if start_time is not None:
                entry.append([start_time.hour, start_time.minute])
            else:
                st.error("Start time is required")
                return
            
            if end_time is not None:
                entry.append([end_time.hour, end_time.minute])
            else:
                st.error("End time is required")
                return
            
            if days:
                entry.append(''.join([days_mapping[day] for day in days]))
            else:
                st.error("At least one day must be selected")
                return

            # Ensure data list has proper structure with name at index 0
            if not st.session_state['data']:
                st.session_state['data'] = [""]
            
            entry_index = int(keyStr) + 1  # +1 because index 0 is the name
            
            # Ensure list is long enough
            while len(st.session_state['data']) <= entry_index:
                st.session_state['data'].append(None)
            
            # Save the entry
            st.session_state['data'][entry_index] = entry
            st.success("Saved!")



for i in range(st.session_state['num_entries']):
    add_entry(str(i))


st.divider()

# Debug info to help diagnose session state issues
with st.expander("Preview File:"):
    st.write(st.session_state['data'])

json_buffer = StringIO()
st.session_state['data'] = [i for i in st.session_state['data'] if i != '']


json.dump(st.session_state['data'], json_buffer)
json_content = json_buffer.getvalue()
st.download_button('Download', json_content, file_name=f"{name}.json", mime='application/json')

