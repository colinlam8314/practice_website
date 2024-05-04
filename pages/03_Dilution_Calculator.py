import streamlit as st

st.markdown("<h1 style='text-align: center;'>Dilution Calculator</h1>", unsafe_allow_html=True)

form = {
    'target': None
}

# Page Layout
left, right = st.columns(2)

# Options
# Main Options
main_options = ['RNA virus', 'DNA targets','other']

# RNA viruses
RNA_virus_options = ['Covid', 'FluA', 'FluB', 'MS2']

# Covid viruses
covid_strain_option = ['gamma-irradiated covid, WA-20']

# Stock Virus concentration
stock_virus = {
    'gamma-irradiated covid, WA-20': int(1.05e6)
}

# Virus selection
with left:

    final_selection = None

    main_selection = st.selectbox(
        'Select the type of virus/bacteria: ',
        main_options,
        index = None,
        placeholder = 'Click to select'
    )

    if main_selection =='RNA virus':
        RNA_virus_selection = st.selectbox(
            'Select the RNA virus: ',
            RNA_virus_options,
            index = None,
            placeholder = 'Click to select'
        )

         # Covid
        if RNA_virus_selection == 'Covid':
            covid_strain_selection = st.selectbox(
                'Select the Covid strain: ',
                covid_strain_option,
                index = None,
                placeholder = 'Click to select'
            )

            final_selection = covid_strain_selection

# Dilution calculation function
st.write(final_selection)