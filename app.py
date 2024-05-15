import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from transformers import pipeline
import requests

st.title("ESG Data Analysis Chatbot")
st.write("Ask me about ESG performance and insights for any stock!")

summarizer = pipeline("summarization")

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    esg_scores = stock.sustainability
    return esg_scores

def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=25, do_sample=False)
    return summary[0]['summary_text']

def get_stock_performance(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    return hist

def plot_esg_scores(esg_data):
    if esg_data is not None:
        esg_scores = esg_data.T
        esg_scores.columns = ['Score']
        sns.barplot(x=esg_scores.index, y='Score', data=esg_scores)
        plt.title('ESG Scores')
        st.pyplot(plt)

def fetch_sustainalytics_esg(ticker):
    api_key = "XXXXX"
    url = f"https://api.sustainalytics.com/esg/{ticker}?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_refinitiv_esg(ticker):
    api_key = "XXXXX"
    url = f"https://api.refinitiv.com/esg/{ticker}?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_msci_esg(ticker):
    api_key = "XXXXX"
    url = f"https://api.msci.com/esg/{ticker}?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_real_esg_data(ticker):
    esg_data = {}
    sustainalytics_data = fetch_sustainalytics_esg(ticker)
    refinitiv_data = fetch_refinitiv_esg(ticker)
    msci_data = fetch_msci_esg(ticker)

    if sustainalytics_data:
        esg_data["Sustainalytics"] = sustainalytics_data
    if refinitiv_data:
        esg_data["Refinitiv"] = refinitiv_data
    if msci_data:
        esg_data["MSCI"] = msci_data

    if esg_data:
        return esg_data
    return None

user_input = st.text_input("Your Question:")

if user_input:
    st.write("Analyzing...")
    
    ticker = user_input.upper()
    
    # Fetch real ESG data
    real_esg_data = fetch_real_esg_data(ticker)
    if real_esg_data:
        # Summarize the real ESG data
        esg_text = f"ESG data for {ticker}: {real_esg_data}"
        summary = summarize_text(esg_text)
        st.write("Summary:", summary)
    else:
        st.write("No ESG data found for this ticker.")
    
    # Get and display ESG data from yfinance
    esg_data = get_stock_data(ticker)
    if esg_data is not None:
        st.write(esg_data)
        plot_esg_scores(esg_data)
    else:
        st.write("No ESG data found for this ticker.")
    
    # Get and display stock performance
    stock_data = get_stock_performance(ticker)
    if not stock_data.empty:
        st.write(f"Stock performance for {ticker}:")
        st.line_chart(stock_data['Close'])
    else:
        st.write(f"No historical data found for {ticker}.")

# Run the Streamlit app with localtunnel
import threading
import subprocess

def run_streamlit():
    subprocess.run(["streamlit", "run", "app.py"])

def run_localtunnel():
    subprocess.run(["lt", "--port", "8501", "--subdomain", "yourcustomsubdomain"])

# Start Streamlit app in a new thread
streamlit_thread = threading.Thread(target=run_streamlit)
streamlit_thread.start()

# Start localtunnel in the main thread
run_localtunnel()
