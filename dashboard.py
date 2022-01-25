import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Prosjekt info',
                   page_icon=":bar_chart:",
                   layout="wide"
)


df = pd.read_excel(
    io='C:\\Users\\NilsAndreasSkreddern\\Desktop\\eXl\\833 Nils Andreas Skreddernes Prosjektliste 2022.xlsx',
    #io='C:\\Users\\Nils\\OneDrive\\Documents\\Programering\\Python\\Excel 2\\eXl\\833 Nils Andreas Skreddernes Prosjektliste 2022.xlsx',
    engine='openpyxl',
    usecols='A:S',
    nrows=10,
    skiprows=14
)

st.title(":bar_chart: Prosjektliste")
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
