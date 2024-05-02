import streamlit as st

st.markdown("<h1 style='text-align: center; color: grey;'>Big headline</h1>", unsafe_allow_html=True)

st.header("LAMP Reagent Calculator")

form = {
    'reactions': None,
    'excess': None,
    'rxn_mm': None
}

# Setting page layout
left, right = st.columns(2)

# Parameter inputs
with left:
    input_number = st.number_input(label= 'Total number of reactions =', min_value = 0, step = 1)
    form['reactions'] = input_number

    # Setting parameters for calculations
    form['excess'] = st.slider('How much in excess (in %):', min_value = 0, max_value = 100, value = 20, step = 1)

    # Total reaction master mix calculation
    total_rxn_mm = int(form['reactions'] * 15 * (1 + (form['excess']/100)))
    form['rxn_mm'] = total_rxn_mm


# Display section
form_disp = {
    'Total number of reactions: ': form['reactions'],
    'Total reaction master mix': form['rxn_mm']
}


# Display results
with right:
    st.write(form_disp)
