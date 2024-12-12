import streamlit as st
import pandas as pd
import pickle
import numpy as np
import joblib




logo = "images.png"
st.image(logo, width = 200)

st.title("Google Ads Predictor")





option = st.selectbox(
    "What would you like to do?",
    (
        "Select an option",
        "1. Predict Cost Per Click, and Conversions (Performance Max Included)",
        "2. Predict Cost Per Click, and Conversions (Search Campaign Only)",
        "3. Predict the Best Keywords"
    ),
)

# Option 1: View Dataset Summary
if option == "1. Predict Cost Per Click, and Conversions (Performance Max Included)":
    def load_model():
     model_path1 = "random_forest_model.pkl"
     with open(model_path1, "rb") as file:
        model = joblib.load("random_forest_model.pkl")
    return model
    model = load_model()
    st.header("Predict Number of Potential Clicks, Cost Per Click And Conversions")
    st.write("Enter the values for the following inputs to predict the outcome:")
    

    # Take input from the user
    #clicks2 = st.number_input("Number of Clicks", min_value=0)
    #avg_cpc = st.number_input("Average Cost Per Click", min_value=0.0, format="%.2f")
    
    Cost = st.number_input("How Much The Client Wants To Spend Per Month?", min_value=0)

    location_mapping = { 'Toronto, Montreal, Vancouver or USA' : 1, 'Brossard, Longueuil, Rive Sud, Laval, West Island, Hamilton, Ottawa, Quebec City, Oshawa, Kitchener, Edmonton, Winnipeg, Calgary, Victoria': 2, 
     'All Other Places (Less Populated Cities and Rural Areas)': 3}
    Location = st.selectbox(
    "Select the Location of Their Campaign:",
    list(location_mapping.keys()) 
    )
    numeric_location = location_mapping[Location]
    season_mapping = {'Winter': 1, 'Summer': 0}
    Season = st.selectbox(
    "Select the Season of Their Campaign:",
    list(season_mapping.keys()) 
    )
    numeric_season = season_mapping[Season]
  



    industry_mapping = {
    'Box Creator': 0, 'Car Mechanic': 1, 'Cleaning': 2, 'Clinic': 3, 'Concrete': 4, 
    'Construction': 5, 'Dentist': 6, 'Disposal': 7, 'Doors & Windows': 8, 
    'Electrician': 9, 'Excavator': 10, 'Exterminator': 11, 'Flooring': 12, 
    'Glass': 13, 'Home Cabinets': 14, 'Home Designer': 15, 'Home Inspection': 16, 
    'Hvac': 17, 'Insulation': 18, 'Landscaper': 19, 'Lawyer': 20, 'Lighting': 21, 
    'Machine Shop': 22, 'Moving Services': 23, 'Other Industries': 24, 'Painter': 25, 
    'Paving': 26, 'Plumber': 27, 'Printer Contractor': 28, 'Renovation': 29, 
    'Roofer': 30, 'Tools': 31, 'Training Classes': 32, 'Transport': 33, 
    'Tree Services': 34, 'Water Softener Shop': 35, 'Welder': 36, 'Well Drilling': 37
    }

    Industry = st.selectbox(
    "Select The Industry of Their Campaign:",
    list(industry_mapping.keys()) )  # Display industry names in the dropdown
    numeric_industry = industry_mapping[Industry]
    # Make predictions based on input
    if st.button("Predict Conversions"):
     input_data = pd.DataFrame({
            "Season_encoded": [numeric_season],
            "Location ID": [numeric_location],
            "Industry_encoded": [numeric_industry],
        })
    
     predicted_conversions2 = model.predict(input_data)
      # Get individual tree predictions
     tree_predictions = np.array([tree.predict(input_data)[0] for tree in model.estimators_])
        
        # Calculate the mean prediction
     mean_prediction = np.mean(tree_predictions)

        # Calculate the prediction interval
     lower_bound = mean_prediction - np.std(tree_predictions) * 0.25  # Approx. 95% confidence
     if lower_bound<0:
         lower_bound = 0
     upper_bound = mean_prediction + np.std(tree_predictions) * 0.25 

        # Display results
     st.success(f"Predicted CPC: {mean_prediction:.2f}")
     st.write(f"Prediction Interval: [{lower_bound:.2f}, {upper_bound:.2f}]")



if option == "2. Predict Cost Per Click, and Conversions (Search Campaign Only)":
    def load_model2():
     model_path2 = "random_forest_model_campaign.pkl"
     with open(model_path2, "rb") as file:
        model2 = joblib.load("random_forest_model_campaign.pkl")
    return model2
    model2 = load_model2()
    st.header("Predict Number of Potential Clicks, Cost Per Click And Conversions")
    st.write("Enter the values for the following inputs to predict the outcome:")
    

    # Take input from the user
    #clicks2 = st.number_input("Number of Clicks", min_value=0)
    #avg_cpc = st.number_input("Average Cost Per Click", min_value=0.0, format="%.2f")
    
    Cost = st.number_input("How Much The Client Wants To Spend Per Month?", min_value=0)

    location_mapping = { 'Toronto, Montreal, Vancouver or USA' : 1, 'Brossard, Longueuil, Rive Sud, Laval, West Island, Hamilton, Ottawa, Quebec City, Oshawa, Kitchener, Edmonton, Winnipeg, Calgary, Victoria': 2, 
     'All Other Places (Less Populated Cities and Rural Areas)': 3}
    Location = st.selectbox(
    "Select the Location of Their Campaign:",
    list(location_mapping.keys()) 
    )
    numeric_location = location_mapping[Location]
    season_mapping = {'Winter': 1, 'Summer': 0}
    Season = st.selectbox(
    "Select the Season of Their Campaign:",
    list(season_mapping.keys()) 
    )
    numeric_season = season_mapping[Season]
  



    industry_mapping = {
    'Box Creator': 0, 'Car Mechanic': 1, 'Cleaning': 2, 'Clinic': 3, 'Concrete': 4, 
    'Construction': 5, 'Dentist': 6, 'Disposal': 7, 'Doors & Windows': 8, 
    'Electrician': 9, 'Excavator': 10, 'Exterminator': 11, 'Flooring': 12, 
    'Glass': 13, 'Home Cabinets': 14, 'Home Designer': 15, 'Home Inspection': 16, 
    'Hvac': 17, 'Insulation': 18, 'Landscaper': 19, 'Lawyer': 20, 'Lighting': 21, 
    'Machine Shop': 22, 'Moving Services': 23, 'Other Industries': 24, 'Painter': 25, 
    'Paving': 26, 'Plumber': 27, 'Printer Contractor': 28, 'Renovation': 29, 
    'Roofer': 30, 'Tools': 31, 'Training Classes': 32, 'Transport': 33, 
    'Tree Services': 34, 'Water Softener Shop': 35, 'Welder': 36, 'Well Drilling': 37
    }

    Industry = st.selectbox(
    "Select The Industry of Their Campaign:",
    list(industry_mapping.keys()) )  # Display industry names in the dropdown
    numeric_industry = industry_mapping[Industry]
    # Make predictions based on input
    if st.button("Predict Conversions"):
     input_data = pd.DataFrame({
            "Season_encoded": [numeric_season],
            "Location ID": [numeric_location],
            "Industry_encoded": [numeric_industry],
        })
    
     predicted_conversions2 = model2.predict(input_data)
      # Get individual tree predictions
     tree_predictions = np.array([tree.predict(input_data)[0] for tree in model2.estimators_])
        
        # Calculate the mean prediction
     mean_prediction = np.mean(tree_predictions)

        # Calculate the prediction interval
     lower_bound = mean_prediction - np.std(tree_predictions) * 0.25  # Approx. 95% confidence
     if lower_bound<0:
         lower_bound = 0
     upper_bound = mean_prediction + np.std(tree_predictions) * 0.25 

        # Display results
     st.success(f"Predicted CPC: {mean_prediction:.2f}")
     st.write(f"Prediction Interval: [{lower_bound:.2f}, {upper_bound:.2f}]")
if option == "3. Predict the Best Keywords":
    
    st.header("In Production ...")
    




