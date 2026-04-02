import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#setting title and page layout
st.set_page_config(page_title="Stock Data Extraction App", layout="wide")

#main title
st.title("Stock Data Extraction App")

#short discription under title
st.write("Extract stock market data from Yahoo Finance using ticker symbol.")

#sidebar header
st.sidebar.header("User Input")

#input box for stock ticker
ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL")

#input for start date
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))

#input for end date
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

#download data button
if st.sidebar.button("Get Data"):

  #create ticker object
  stock = yf.Ticker(ticker)

  #download historical price data
  df = stock.history(start=start_date, end=end_date)

  #check if data exists
  if df.empty:
    st.error("No data found. Please check the ticker symbol or date range.")

    else:

      #show success message
      st.success(f"Data successfully extracted for {ticker}.")

      #display company information
      st.subheader("Company Information")
      info = stock.info

      company_name = info.get("longName", "N/A")
      sector = info.get("sector", "N/A")
      industry = info.get("industry", "N/A")
      market_cap = info.get("marketCap", "N/A")
      website = info.get("website", "N/A")

      st.write(f"**Company Name:** {company_name}")
      st.write(f"**Sector:** {sector}")
      st.write(f"**Industry:** {industry}")
      st.write(f"**Market Cap:** {market_cap}")
      st.write(f"**Website:** {website}")

      #display stock data
      st.subheader(historical Stock Data")
      st.dataframe(df)

      #plot closing price
       st.subheader("Closing Price Chart")
       fig, ax = plt.subplots()
      ax.plot(df.index, df["Close"])
      ax.set_xlabel("Date")
       ax.set_ylabel("Closing Price")
      st.set_title(f"{ticker} Closing Price")
     st.pyplot(fig)

        #convert datafram to CSV for download
        csv = df.to_csv().encode("utf-8")

      #download button for CSV
      st.download_button(
          label="Download Data as CSV",
          data=csv,
          file_name=f"{ticker}_stock_data.csv",
          mime="text/csv" 
      )
