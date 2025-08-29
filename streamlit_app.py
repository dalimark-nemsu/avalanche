# Main UI and logic for the Streamlit app
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.title("Customer Reviews Analyzer")

# Load data
def load_data():
    # data_path = os.path.join("data", "customer_reviews.csv")
    data_path = "customer_reviews.csv"
    
    if os.path.exists(data_path):
        return pd.read_csv(data_path)
    else:
        st.warning("No customer_reviews.csv found in data directory.")
        return pd.DataFrame()

df = load_data()
if not df.empty:
    st.write("### Example Customer Reviews", df.head())
else:
    st.info("Upload or add your customer reviews data.")

# Add your app logic here (e.g., sentiment analysis, summarization, etc.)

