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

st.header('Legg til prosjektinfo')

prod_dict['Addresse'] = st.text_input('Addresse')

col1, col2 = st.beta_columns(2)
with col1:
    prod_dict['Postnummer'] = st.text_input('Postnummer')
with col2:
    prod_dict['Poststed'] = st.text_input('Poststed')


col21, col22 = st.beta_columns(2)
with col21:
    prod_dict['Type'] =  st.selectbox(
        'Type',
        ('Fakturerbar', 'Reklamasjon', 'Internt'))


with col22:
    prod_dict['Årsak'] = st.selectbox(
        'Skadeårsak',
        ('Vann', 'Skadedyr', 'Håndverk', 'Innbo/Løsøre', 'Reklamasjon')        
    )


col31, col32 = st.beta_columns(2)
with col31:
    prod_dict['Selskap'] = st.selectbox(
        'Forsikringsleskap',
        ('IF Skadeforsikring', 'Gjensidige', 'KLP', 'Insr', 'Tryg', 'Frende', 'Landkreditt')
    )

with col32:
    prod_dict['Skadenummer'] = st.text_input('Skadenummer')