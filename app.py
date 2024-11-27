import streamlit as st
import pandas as pd
import pickle


logo = "images.png"
st.image(logo, width = 200)

st.title("Google Ads Predictor")


def load_model():
    with open("random_forest_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model


model = load_model()


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
    clicks2 = st.number_input("Number of Clicks", min_value=0)
    avg_cpc = st.number_input("Average Cost Per Click", min_value=0.0, format="%.2f")
    impressions = st.number_input("Number of Impressions", min_value=0)

    # Make predictions based on input
    if st.button("Predict Conversions"):
     input_data = pd.DataFrame({
            "Clicks": [clicks2],
            "Avg. CPC": [avg_cpc],
            "Impr.": [impressions],
        })
     predicted_conversions =  0.031134*clicks2 + -0.662742 * avg_cpc -0.000064*impressions + 12.1954
     predicted_conversions2 = model.predict(input_data)
     
     
    
     st.write(f"Predicted Conversions based on linear regression: {predicted_conversions}")
     st.write(f"Predicted Conversions based on random forest: {predicted_conversions2}")




