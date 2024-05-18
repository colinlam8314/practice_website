import streamlit as st
import pandas as pd
from datetime import datetime


# for sample_type_df in sample_types:
#     edited_df = st.data_editor(sample_type_df)
df = {
    "rna target": [
        {
            "index": "covid",
            "strain": "ab",
            "lot": "!234342",
            "date received": datetime.today() 
        }
    ]
}

loaded_df = pd.DataFrame(df['rna target'])

# sample_types = []
# for sample_type in loaded_df.columns:
#     sample_types.append(loaded_df[sample_type])

# st.write(sample_types)
st.data_editor(loaded_df,hide_index=True)