from re import A
import pandas as pd
import plotly.express as px
import streamlit as st

prod_dict = {
    'Addresse'      : '',
    'Postnummer'    : '',
    'Poststed'      : '',
    'Selskap'       : '',
    'Type'          : '',
    'Skadenummer'   : '',
    'Kunde'         : '',
    'Årsak'         : ''
}

fakt_dict = {
    'Info'      : '',
    'Antall'    : '',
    'Type'      : '',
    'Verdi'     : ''
}

st.header('Legg til prosjektinfo')

prod_dict['Addresse'] = st.text_input('Addresse')

col1, col2 = st.columns(2)
with col1:
    prod_dict['Postnummer'] = st.text_input('Postnummer')
with col2:
    prod_dict['Poststed'] = st.text_input('Poststed')


col21, col22 = st.columns(2)
with col21:
    prod_dict['Type'] =  st.selectbox(
        'Type',
        ('Fakturerbar', 'Reklamasjon', 'Internt'))


with col22:
    prod_dict['Årsak'] = st.selectbox(
        'Skadeårsak',
        ('Vann', 'Skadedyr', 'Håndverk', 'Innbo/Løsøre', 'Reklamasjon', 'Annet')
    )


col31, col32 = st.columns(2)
with col31:
    prod_dict['Selskap'] = st.selectbox(
        'Forsikringsleskap',
        ('IF Skadeforsikring', 'Gjensidige', 'KLP', 'Insr', 'Tryg', 'Frende', 'Landkreditt')
    )

with col32:
    prod_dict['Skadenummer'] = st.text_input('Skadenummer')

st.button("Opprett")

st.header('Faktura')
fakt_dict['Info'] = st.text_input('Info')

col41, col42, col43 = st.columns(3)

with col41:
    fakt_dict['Antall'] = st.text_input('Antall')

with col42:
    fakt_dict['Type'] = st.selectbox(
        'Type',
        ('sum', 'stk', 'km', 'rundsum')
    )

with col43:
    fakt_dict['Verdi'] = st.text_input('Pris/sum')

col51, col52 = st.columns(2)
with col51:
    st.button('Legg til linje')

with col52:
    st.button('Opprett faktura')
