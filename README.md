# AI-Powered-Chatbot-for-Advanced-ESG-Analysis-and-Reporting

## Overview
The Streamlit-Powered ESG Data Analysis Chatbot is an interactive web application designed to provide insights into the Environmental, Social, and Governance (ESG) performance of publicly traded companies. Leveraging APIs from ESG data providers such as Sustainalytics, Refinitiv, and MSCI, as well as financial data from Yahoo Finance, this tool offers users detailed ESG scores, summaries, and visualizations for specified stock tickers.

## Project Features
- **Interactive User Interface**: Built with Streamlit, allowing users to input stock ticker symbols effortlessly.
- **Real-time ESG Data Retrieval**: Fetches ESG scores from Sustainalytics, Refinitiv, and MSCI.
- **Financial Data Analysis**: Retrieves and visualizes historical stock performance data from Yahoo Finance.
- **Text Summarization**: Utilizes NLP techniques to summarize ESG reports and insights.
- **Data Visualization**: Provides clear and informative visualizations of ESG scores and stock performance.

## Technical Details
### Libraries and Tools
- **Streamlit**: For building the interactive web application.
- **transformers**: For NLP tasks, including text summarization.
- **yfinance**: For retrieving financial data.
- **matplotlib**: For creating visualizations.
- **seaborn**: For enhancing visualizations.
- **localtunnel**: For exposing the Streamlit app to the web.
- **requests**: For making API calls to ESG data providers.

### ESG Data Providers
- **Sustainalytics**: Provides ESG scores and reports.
- **Refinitiv**: Offers comprehensive ESG data.
- **MSCI**: Delivers ESG ratings and insights.

### Data Preprocessing
1. **Fetching Data**: Uses API calls to retrieve ESG data from multiple providers.
2. **Summarizing Text**: Employs the transformers library for text summarization to generate concise ESG reports.

## Setup Instructions

### Requirements
- Python 3.x
- Streamlit
- transformers
- yfinance
- matplotlib
- seaborn
- localtunnel
- requests
- API keys for ESG data providers (Sustainalytics, Refinitiv, MSCI)
