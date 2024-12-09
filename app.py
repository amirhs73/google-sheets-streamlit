import streamlit as st
import pandas as pd
import pickle
import numpy as np
import os



logo = "images.png"
st.image(logo, width = 200)

st.title("Google Ads Predictor")



def load_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current script directory
    model_path = os.path.join(current_dir, "random_forest_model.pkl")  # Build full path
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()


option = st.selectbox(
    "What would you like to do?",
    (
        "Select an option",
        "1. Predict Number of Potential Clicks, Cost Per Click, and Conversions",
        "2. Predict the Best Keywords"
    ),
)

# Option 1: View Dataset Summary
if option == "1. Predict Number of Potential Clicks, Cost Per Click, and Conversions":
    st.header("Predict Number of Potential Clicks, Cost Per Click And Conversions")
    st.write("Enter the values for the following inputs to predict the outcome:")
    

    # Take input from the user
    #clicks2 = st.number_input("Number of Clicks", min_value=0)
    #avg_cpc = st.number_input("Average Cost Per Click", min_value=0.0, format="%.2f")
    
    Cost = st.number_input("How Much The Client Wants To Spend Per Month?", min_value=0)

    location_mapping = { "Toronto, Montreal, Vancouver or USA" : 1, "Brossard, Longueuil, Rive Sud, Laval, West Island, Hamilton, Ottawa, Quebec City, Oshawa, Kitchener, Edmonton, Winnipeg, Calgary, Victoria":2, 
     "All Other Places (Less Populated Cities and Rural Areas)":3}
    Location = st.selectbox(
    "Select the Location of Their Campaign:",
    list(location_mapping.keys()) 
    )
    Season = st.selectbox(
    "Select the Season of Their Campaign:",
    ["Winter", "Summer"]
    )

  



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
    
    # Make predictions based on input
    if st.button("Predict Conversions"):
     input_data = pd.DataFrame({
            "Cost": [Cost],
            "Location": [Location],
            "Industry": [Industry],
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
     st.success(f"Predicted Conversions: {mean_prediction:.2f}")
     st.write(f"Prediction Interval: [{lower_bound:.2f}, {upper_bound:.2f}]")
   
if option == "2. Predict the Best Keywords":
    
    st.header("In Production ...")
    




