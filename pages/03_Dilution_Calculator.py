import streamlit as st
import pandas as pd
import numpy as np
import json

# Load json file
with open('config.json','r') as file:
    load_data = json.load(file)

st.markdown("<h1 style='text-align: center;'>Dilution Calculator</h1>", unsafe_allow_html=True)


# Dilution calculation function
# def dilute_calc(conc, wanted_conc):
#     if wanted_conc <= 0:
#         st.markdown("Please input a valid number")

#     volume = (2*conc)/wanted_conc

#     if volume >= 50 and volume <= 1000:
#         volume = volume - 2
#         # st.write('2 uL ',conc,' + ',volume,'uL H2O --> ',volume+2,' E4 cp/uL')
#         st.markdown(f'2 uL <mark><b>{conc:.2e}</b></mark> cp/uL + <mark><b>{volume}</b></mark> uL H2O --> <mark><b>{volume+2}</b></mark> <mark><b>{wanted_conc:.2e}</b></mark> cp/uL',unsafe_allow_html=True)

#     if volume > 1000:
#         conc_dilute_100x = conc/100
#         st.markdown(f'2 uL <mark><b>{conc:.2e}</b></mark> cp/uL stock + 198 uL H2O --> 200 uL <mark><b>{conc_dilute_100x:.2e}</b></mark> cp/uL', unsafe_allow_html=True)
#         dilute_calc(conc_dilute_100x, wanted_conc)

#     if volume < 50 and volume > 2 and conc != float(final_conc):
#         conc_dilute_10x = conc/10
#         st.markdown(f'20 uL <mark><b>{conc:.2e}</b></mark> cp/uL stock + 180 uL H2O --> 200 uL <mark><b>{conc_dilute_10x:.2e}</b></mark> cp/uL', unsafe_allow_html=True)
#         dilute_calc(conc_dilute_10x, wanted_conc) 
#     elif conc == float(final_conc) and volume < 50 and volume > 2:
#         volume = volume - 2
#         # st.write('2 uL ',conc,' + ',volume,'uL H2O --> ',volume+2,' E4 cp/uL')
#         st.markdown(f'2 uL <mark><b>{conc:.2e}</b></mark> cp/uL + <mark><b>{volume}</b></mark> uL H2O --> <mark><b>{volume+2}</b></mark> <mark><b>{wanted_conc:.2e}</b></mark> cp/uL',unsafe_allow_html=True)
#         st.markdown("Starting concentration might be too diluted. Consider changing the desired concentration or use a more concentrated stock.")
#     else:
#         st.markdown("Input an appropriate target concentration!")

dilution_num = 0

def dilute_calc(conc, wanted_conc):
    volume = (2*conc)/wanted_conc
    count = dilution_num

    if volume >= 50 and volume <= 1000:
        volume = volume - 2
        # st.write('2 uL ',conc,' + ',volume,'uL H2O --> ',volume+2,' E4 cp/uL')
        st.markdown(f'2 uL <mark><b>{conc:.2e}</b></mark> cp/uL + <mark><b>{volume}</b></mark> uL H2O --> <mark><b>{volume+2}</b></mark> <mark><b>{wanted_conc:.2e}</b></mark> cp/uL',unsafe_allow_html=True)

    if volume < 50 and count == 0:
        st.write("Starting concentration is too low!")

    if volume < 50 and count > 0:
        conc = conc*10
        dilute_calc(conc, wanted_conc)
        return count
        




    # volume = (2*conc)/wanted_conc
    # if volume > 1000:
    #     conc_dilute_100x = conc/100
    #     st.markdown(f'2 uL <mark><b>{conc:.2e}</b></mark> cp/uL stock + 198 uL H2O --> 200 uL <mark><b>{conc_dilute_100x:.2e}</b></mark> cp/uL', unsafe_allow_html=True)
    #     dilute_calc(conc_dilute_100x, wanted_conc)
    # # elif volume < 12 and conc > 0:
    # #     conc_dilute_10x = conc/10
    # #     st.markdown(f'20 uL <mark><b>{conc:.2e}</b></mark> cp/uL stock + 180 uL H2O --> 200 uL <mark><b>{conc_dilute_10x:.2e}</b></mark> cp/uL', unsafe_allow_html=True)
    # #     dilute_calc(conc_dilute_10x, wanted_conc)
    # else:
    #     volume = volume - 2
    #     # st.write('2 uL ',conc,' + ',volume,'uL H2O --> ',volume+2,' E4 cp/uL')
    #     st.markdown(f'2 uL <mark><b>{conc:.2e}</b></mark> cp/uL + <mark><b>{volume}</b></mark> uL H2O --> <mark><b>{volume+2}</b></mark> <mark><b>{wanted_conc:.2e}</b></mark> cp/uL',unsafe_allow_html=True)
    #     return volume


# Load options for tarfet type
sample_types = list(load_data.keys())

# Selectbox for sample types
sample_type = st.selectbox("Select type of virus", sample_types, placeholder='Click to select')

# Get the targets for the selected sample type
targets = pd.DataFrame(load_data[sample_type])
target_selections = pd.unique(targets["Type"])
st.write(targets)

# Selectbox for target
targets_select = st.selectbox("Select target", target_selections, placeholder="Click to select")


# Get the strains for the selected target
strains = targets[targets["Type"] == targets_select]
st.write(strains)
strain_selections = pd.unique(strains["Strain"])
st.write(strain_selections)

# Selectbox for strain
strain_select = st.selectbox("Select strain", strain_selections, placeholder="Click to select")

# Output concentration of selected strain
final_selection = strains[strains["Strain"] == strain_select]
st.write(final_selection)
final_conc = final_selection["Concentration (cp/uL)"]
st.write((final_conc))

# Asking the final concentration wanted
desired_conc = st.number_input("Final target concentration (cp/uL) ",value = 5.0, min_value=0.0, placeholder= "Input number here")

dilute_calc(float(final_conc.iloc[0]), desired_conc)