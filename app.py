import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials



# Load data and perform analysis
st.title("Google Sheets Data Analysis App")

st.write("Data from Google Sheets:")


# Perform analysis or add interactive elements here
st.write("Summary Statistics:")
st.write(data.describe())
