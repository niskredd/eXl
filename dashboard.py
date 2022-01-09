import pandas as pd
import plotly.express as px
import sreamlit as st

st.set_page_config(page_title='Prosjekt info',
                   page_icon=":bar_chart:",
                   layout="wide"
)



df = pd.read_excel(
    io='book.xlsx',
    engine='openpyxl',
    sheet_name='Fylles ut først',
    usecols='A:D',
    nrows=20,
)


st.dataframe(df)


# ---- Sidebar ----
st.sidebar.header("Plese Filter Here:")
company = st.sidebar.multiselect(
    "Select Company:",
    option=df[''].unique(),
    defalut=df[''].unique()
)

active = st.sidebar.multiselect(
    "Select Status:",
    option=df[''].unique(),
    defalut=df[''].unique()
)

df_selection = df.query(
    "Company == @company & Status == @active"
)


st.title(":bar_chart: Prosjekt Dashbord")
st.markdown("##")


totale = int(df_selection['Fakturert'].sum())
