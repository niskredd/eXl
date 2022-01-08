import pandas as pd
import plotly.express as px
import sreamlit as st

df = pd.read_excel(
    io='book.xlsx',
    engine='openpyxl',
    sheet_name='Fyll ut først',
    usecols='A:D',
    nrows=20,
)


print(df)