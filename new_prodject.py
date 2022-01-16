from re import A
import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Legg til prosjektinfo')

address = st.text_input('Addresse')

col1, col2 = st.columns(2)
with col1:
    post_nr = st.text_input('Postnummer')
with col2:
    city = st.text_input('Poststed')


col21, col22 = st.columns(2)
with col21:
    oe_type =  st.selectbox(
        'Type',
        ('Fakturerbar', 'Reklamasjon', 'Internt'))


with col22:
    cause = st.selectbox(
        'Skadeårsak',
        ('Vann', 'Skadedyr', 'Håndverk', 'Innbo/Løsøre', 'Reklamasjon')        
    )


col31, col32 = st.columns(2)
with col31:
    company = st.selectbox(
        'Forsikringsleskap',
        ('IF Skadeforsikring', 'Gjensidige', 'KLP', 'Insr', 'Tryg', 'Frende', 'Landkreditt')
    )

with col32:
    com_referance = st.text_input('Skadenummer')