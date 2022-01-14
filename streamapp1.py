import streamlit as st
import pandas as pd
import yfinance as yf

st.write("""
    # Simple Stock price app
    # 
    # 
    # Shown are the stock closing pirce and volume of google
    # 
    # """)



tickerSymbol = 'FKRFT.OL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2021-12-14', end='2022-1-14')



st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

