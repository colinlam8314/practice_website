import streamlit as st

st.header("qPCR Reagent Calculator")

form = {
    "reactions": None,
    "rxn_mm": None,
    "excess": None,
    "dye": None,

    # Reagent Breakdown
    "luna_mm": None,
    "primer_mix":None,
    "evagreen":None,
    "water": None
}

# Setting page layout
left, right = st.columns(2)

# Container for inputs on the left column
with left:

    # Input number of reactions
    input_number = st.number_input(label= 'Total number of reactions =', min_value = 0, step = 1)
    form['reactions'] = input_number

    # Confirming whether primer mix already contains a dye or not
    on = st.toggle('Is there dye in the primer mix?')

    if on:
        form['dye'] = "Yes"
        st.write('Dye is in the mix')
    else:
        form['dye'] = "No"
        st.write('No dye is in the mix')

    # Setting parameters for calculations
    form['excess'] = st.slider('How much in excess (in %):', min_value = 0, max_value = 100, value = 20, step = 1)

    # Calculate total amount of reaction master mix
    total_rxn_mm = int(form['reactions'] * 15 * (1 + (form['excess']/100)))
    form['rxn_mm'] = total_rxn_mm

    # Calculating individual components
    form["luna_mm"] = total_rxn_mm / 3
    form["primer_mix"] = total_rxn_mm / 1.5
    form["evagreen"] = total_rxn_mm / 30
    form["water"] = (total_rxn_mm / 3) - form["evagreen"]

# st.write(f'selected text is: {selected_text}')
# st.write(f'input text is: {input_text}')


# Display section

# Without dye in primer mix
form_disp_no_dye = {
    "Total reactions": form["reactions"],
    "Total reaction mastermix": form["rxn_mm"],
    "4x LUNA MM to add: ": form["luna_mm"],
    "4x primer mix to add: ": form["primer_mix"]
}

# With dye in primer mix
form_disp_dye = {
    "Total reactions": form["reactions"],
    "Total reaction mastermix": form["rxn_mm"],
    "4x LUNA MM to add: ": form["luna_mm"],
    "4x primer mix to add: ": form["primer_mix"],
    "20x Evagreen to add: ": form["evagreen"],
    "Water to add: ": form["water"]
}


# Display results on the right side
with right:
    if form['dye'] == 'Yes':
        st.write(form_disp_no_dye)
    else:
        st.write(form_disp_dye)
