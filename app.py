import streamlit as st
import pandas as pd
import pickle
import numpy as np


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
    
     predicted_conversions2 = model.predict(input_data)
      # Get individual tree predictions
     tree_predictions = np.array([tree.predict(input_data)[0] for tree in model.estimators_])
        
        # Calculate the mean prediction
     mean_prediction = np.mean(tree_predictions)

        # Calculate the prediction interval
     lower_bound = mean_prediction - np.std(tree_predictions) * 0.25  # Approx. 95% confidence
     upper_bound = mean_prediction + np.std(tree_predictions) * 0.25 

        # Display results
     st.success(f"Predicted Conversions: {mean_prediction:.2f}")
     st.write(f"Prediction Interval: [{lower_bound:.2f}, {upper_bound:.2f}]")
   

    
     
    




