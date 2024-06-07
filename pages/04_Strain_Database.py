import streamlit as st
import pandas as pd
from datetime import datetime
import json

# Function to load data from JSON file
def load_data():
    with open('config.json', 'r') as f:
        return json.load(f)

# Function to save data to JSON file
def save_data(data):
    with open('config.json', 'w') as f:
        json.dump(data, f, indent=4)

data = load_data()

# Create a data editor for each table
st.title("Target Info Database")

for table_name in data.keys():
    st.subheader(f"{table_name}")
    
    # Display data editor and allow editing
    edited_data = st.data_editor(
        data[table_name],
        column_config={"Concentration (cp/uL)": st.column_config.NumberColumn(min_value=0, format="%e")}, 
        num_rows="dynamic", 
        use_container_width=True,
        key= table_name,
    )
    # # Save updated data if there are changes
    if st.button(f"Save {table_name}"):
        data[table_name] = edited_data
        save_data(data)
        st.success(f"{table_name} data saved successfully!")