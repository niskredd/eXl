import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Prosjekt info',
                   page_icon=":bar_chart:",
                   layout="wide"
)



df = pd.read_excel(
    io='C:\\Users\\NilsAndreasSkreddern\\Frøiland Bygg Skade AS\\FBS Fellesområde - 833 Nils Andreas Skreddernes\\833 Nils Andreas Skreddernes Prosjektliste 2022.xlsx',
    engine='openpyxl',
    usecols='A:S',
    nrows=30,
    skiprows=14
)


st.dataframe(df.astype(str))


# ---- Sidebar ----
st.sidebar.header("Plese Filter Here:")
company = st.sidebar.multiselect(
    "Select Company:",
    option=df['IF Skadeforsikring', 'Gjensidige', 'Tryg', 'KLP', 'Knif', 'Landkreditt'].unique(),
    defalut=df[None].unique()
)

active = st.sidebar.multiselect(
    "Select Status:",
    option=df[ 'Besiktiget', 'Klakulert', 'Arbidpågår', 'Klar til fakurering', 'Ferdig'].unique(),
    defalut=df['Besiktiget', 'Klakulert', 'Arbidpågår', 'Klar til fakurering', 'Ferdig'].unique()
)

df_selection = df.query(
    "Company == @company & Status == @active"
)


st.title(":bar_chart: Prosjekt Dashbord")
st.markdown("##")


totale = int(df_selection['Fakturert'].sum())
