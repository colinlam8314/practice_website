import streamlit as st
import pandas as pd

df = pd.read_json('config.json')

edited_df = st.data_editor(df)
