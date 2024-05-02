import streamlit as st

st.markdown("<h1 style='text-align: center;'>LAMP Reagent Calculator</h1>", unsafe_allow_html=True)

form = {
    'reactions': None,
    'beads': None,
    'conditions': None,
    'repeats': None,
    'excess': None,
    'rxn_mm': None,
    'template': None,
    'buffer': None,
    'evagreen': None,
    'primer': None
}

# Setting page layout
left, right = st.columns(2)

# Parameter inputs
with left:
    input_number = st.number_input(label= 'Total number of reactions =', min_value = 0, step = 1)
    form['reactions'] = input_number
    form['beads'] = input_number / 2

    # Conditions and repeats
    form['conditions'] = st.number_input(label= 'How many conditions? ', min_value = 1, value = 1, step = 1)
    form['repeats'] = st.number_input(label = 'How many repeats? ', min_value = 1, value = 4, step = 2)

    # Setting parameters for calculations
    form['excess'] = st.slider('How much in excess (in %):', min_value = 0, max_value = 100, value = 20, step = 1)


    # Reaction master mix per condition calculation: 
    min_rxn_mm = (form['repeats'] / 2) * 50 * (1 + (form['excess']/100))
    make_rxn_mm = min_rxn_mm * 0.75
    
    form['rxn_mm'] = int(make_rxn_mm)
    form['template'] = (form['rxn_mm'])/3

# Display section
form_disp = {
    'Total number of reactions': form['reactions'],
    'Total number of beads': form['beads'],
    'Reaction master mix per condition': form['rxn_mm'],
    'Template to add per condition': form['template']
}


# Display results
with right:
    if (form['conditions'] * form['repeats']) != form['reactions']:
        st.write('Number of conditions and repeats are not matching with total number of reactions.')
    else:
        st.write(form_disp)
