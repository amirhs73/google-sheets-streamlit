import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import openpyxl


logo = "images.png"
st.image(logo, width = 200)

st.title("Google Ads Predictor")
file_url = "PPC Sales Collateral"

# Load the Excel file
data = pd.read_excel(file_url, engine='openpyxl')  # Specify engine='openpyxl' for .xlsx files




features = ['Clicks', 'Avg. CPC', 'Impr.']
X = data[features]
y = data['Conversions']
st.write(y)
# Train-test split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.02, random_state=42)



option = st.selectbox(
    "What would you like to do?",
    (
        "Select an option",
        "1. Predict Conversions",
        "2. Predict Number of Clicks",
        "3. Predict Cost Per Click"
    ),
)

# Option 1: View Dataset Summary
if option == "1. Predict Conversions":
    st.header("Predict Conversions")
    st.write("Enter the values for the following inputs to predict the number of conversions:")
    

    # Take input from the user
    clicks = st.number_input("Number of Clicks", min_value=0)
    avg_cpc = st.number_input("Average Cost Per Click", min_value=0.0, format="%.2f")
    impressions = st.number_input("Number of Impressions", min_value=0)

    # Make predictions based on input
    if st.button("Predict Conversions"):
     new_data = pd.DataFrame({
        'Clicks': [clicks],
        'Avg. CPC': [avg_cpc],
        'Impr.': [impressions]
    })
    predicted_conversions =  0.031134*clicks + -0.662742 * avg_cpc -0.000064*impressions + 12.1954
    #model = RandomForestRegressor(n_estimators=100, random_state=42)
    #model.fit(X_train, y_train)
    st.write(f"Predicted Conversions: {predicted_conversions}")





