#app.py
import dashboard
import new_prodject
import streamlit as st
from streamlit_pages.streamlit_pages import MultiPage

"""PAGES = {
    "Prosjektliste" : dashboard,
    "Legg til nytt prosjekt" : new_prodject
}
st.sidebar.title('Valg')
selection = st.sidebar.radio("Gå til ...", list(PAGES.keys()))
pages = PAGES[selection]

"""

def dashdef():
    if st.button("Dashbord"):
        st.write(dashboard)


def newdef():
    if st.button("Nytt prosjekt"):
        st.write(new_prodject)


# call app class object
app = MultiPage()
# Add pages
app.add_page("Dashbord", dashdef)
app.add_page("Nytt prosjekt", newdef)
app.run()