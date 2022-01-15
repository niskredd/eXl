import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Prosjekt info',
                   page_icon=":bar_chart:",
                   layout="wide"
)


df = pd.read_excel(
    #io='C:\\Users\\NilsAndreasSkreddern\\Frøiland Bygg Skade AS\\FBS Fellesområde - 833 Nils Andreas Skreddernes\\833 Nils Andreas Skreddernes Prosjektliste 2022.xlsx',
    io='C:\\Users\\Nils\\OneDrive\\Documents\\Programering\\Python\\Excel 2\\eXl\\833 Nils Andreas Skreddernes Prosjektliste 2022.xlsx',
    engine='openpyxl',
    usecols='A:S',
    nrows=200,
    skiprows=14
)

st.title(":bar_chart: Prosjekt Dashbord")
st.header("2022")
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
st.dataframe(df.astype(str))


# ---- Sidebar ----
st.sidebar.header("Plese Filter Here:")
company = st.sidebar.multiselect(
    "Velg Selskap:",
    options=df['Selskap'].unique(),
    default=df['Selskap'].unique()
)

state = st.sidebar.multiselect(
    "Velg Status:",
    options=df['Status på skadesaken'].unique(),
    default=df['Status på skadesaken'].unique()
)

df_selection = df.query(
    "Selskap == @company & 'Status på skadesaken' == @state"
)





totale = int(df_selection['Fakturert'].sum())
