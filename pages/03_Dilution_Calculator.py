import streamlit as st
import json

with open('config.json','r') as file:
    load_data = json.load(file)

st.markdown("<h1 style='text-align: center;'>Dilution Calculator</h1>", unsafe_allow_html=True)


# Dilution calculation function
def dilute_calc(conc):
    volume = (2*conc)/1e4
    if volume > 1000:
        conc_dilute_100x = conc/100
        st.markdown(f'2 uL <mark><b>{conc:.2e}</b></mark> cp/uL stock + 198 uL H2O --> 200 uL <mark><b>{conc_dilute_100x:.2e}</b></mark> cp/uL', unsafe_allow_html=True)
        dilute_calc(conc_dilute_100x)
    else:
        volume = volume - 2
        # st.write('2 uL ',conc,' + ',volume,'uL H2O --> ',volume+2,' E4 cp/uL')
        st.markdown(f'2 uL <mark><b>{conc:.2e}</b></mark> + <mark><b>{volume}</b></mark> uL H2O --> <mark><b>{volume+2}</b></mark> E4 cp/uL',unsafe_allow_html=True)
        return volume


# Load sample data
sample_types = load_data

# Display the loaded data (optional, for debugging)
# st.write(sample_types)

# Selectbox for sample types
sample_type = st.selectbox("Select type of virus", list(sample_types.keys()), placeholder='Click to select')

# Get the targets for the selected sample type
if sample_type:
    target_names = sample_types[sample_type]
    target_name = st.selectbox('Select virus', target_names, placeholder='Click to select')




# st.write(load_data)
# sample_types = load_data
# sample_type = st.selectbox("Select type of virus", sample_types, placeholder= 'Click to select', index = None)
# targets = sample_types[sample_type]
# target_names = targets
# target_name = st.selectbox('Select virus', target_names, placeholder= 'Click to select', index = None)
# strains = targets.get(target_name, {})
# strain_names = strains.keys() 
# strain_name = st.selectbox('Select strain', strain_names, placeholder = 'Click to select', index = None)
# selected_strain_conc = strains.get(strain_name, None)

# if strain_name:
#     dilute_calc(selected_strain_conc.get('concentration'))