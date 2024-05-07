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
    'gamma-irradiated covid, WA-20': int(1.05e8)
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
def dilute_calc(conc):
    volume = (2*conc)/1e4
    if volume > 1000:
        conc_dilute_100x = conc/100
        # st.write('2 uL stock ',final_selection,' + 198 uL H2O --> 200 uL ',conc_dilute_100x,' cp/uL')
        # st.write(f'2 uL stock: ', st.markdown(''':blue-blackground[{final_selection}]''') '+ 198 uL H2O --> 200 uL {conc_dilute_100x:.2e} cp/uL')
        variable = 'abc'
        st.markdown(f'fff<mark><b>{variable}</b></mark>', unsafe_allow_html=True)
        dilute_calc(conc_dilute_100x)
    else:
        volume = volume - 2
        st.write('2 uL ',conc,' + ',volume,'uL H2O --> ',volume+2,' E4 cp/uL')
        return volume
    

if final_selection:
    dilute_calc(stock_virus.get(final_selection))