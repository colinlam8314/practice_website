import streamlit as st

form = {
    "reactions": None,
    "rxn_mm": None,
    "excess": None,
    "content": None
}



left, right = st.columns(2)

with left:
    st.header("qPCR Reagent Calculator")

    # Input number of reactions
    input_number = st.number_input(label= 'Total number of reactions=', min_value = 0, step = 1)
    form['reactions'] = input_number

    # Setting parameters for calculations
    form['excess'] = st.slider('How much in excess (in %):', min_value = 0, max_value = 100, value = 20, step = 1)

    # Calculate total amount of reaction master mix
    total_rxn_mm = int(form['reactions'] * 15 * (1 + (form['excess']/100)))
    form['rxn_mm'] = total_rxn_mm

    selected_text = st.selectbox(label= 'content=', options= ['abc', 'def'])
    form['content'] = selected_text

# st.write(f'selected text is: {selected_text}')
# st.write(f'input text is: {input_text}')


# Display section

form_disp = {
    "Total reactions": form["reactions"],
    "Total reaction mastermix": form["rxn_mm"]
}

with right:
    st.write(form_disp)