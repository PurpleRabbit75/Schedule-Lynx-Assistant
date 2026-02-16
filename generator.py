import streamlit as st
import json
from io import StringIO


data = []

name = st.text_input("Name:")
data.append(name)



json_buffer = StringIO()
json.dump(data, json_buffer)
json_content = json_buffer.getvalue()

st.download_button('Download', json_content, file_name=f"{name}.json", mime='application/json')

