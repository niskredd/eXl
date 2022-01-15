#app.py
import dashboard
import new_prodject
import streamlit as st
PAGES = {
    "Prosjektliste" : dashboard,
    "Legg til nytt prosjekt" : new_prodject
}
st.sidebar.title('Valg')
selection = st.sidebar.radio("Gå til ...", list(PAGES.keys()))
pages = PAGES[selection]


