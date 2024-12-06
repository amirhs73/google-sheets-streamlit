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
        "1. Predict Number of Potential Clicks, Cost Per Click And Conversions",
        "2. Predict the best keywords"
    ),
)

# Option 1: View Dataset Summary
if option == "1. Predict Number of Potential Clicks, Cost Per Click And Conversions":
    st.header("Predict Number of Potential Clicks, Cost Per Click And Conversions")
    st.write("Enter the values for the following inputs to predict the number of conversions:")
    

    # Take input from the user
    #clicks2 = st.number_input("Number of Clicks", min_value=0)
    #avg_cpc = st.number_input("Average Cost Per Click", min_value=0.0, format="%.2f")
    
    Cost = st.number_input("How Much The Client Wants To Spend Per Month?", min_value=0)
    location = st.selectbox(
    "Select the Location of Their Campaign:",
    ["Toronto, Montreal, Vancouver or USA", "Brossard, Longueuil, Rive Sud, Laval, West Island, Hamilton, Ottawa, Quebec City, Oshawa, Kitchener, Edmonton, Winnipeg, Calgary ", 
     "All Other Places (Less Populated Cities and Rural Areas)"]
    )
    Industry = st.selectbox(
    "Select the Industry of Their Campaign:",
    ["Roofer", "Construction", "Excavator", "Hvac", "Renovation", "Cleaning", "Tree Services", "Plumber", "Moving Services", "Landscaper", "Car Mechanic", "Flooring", "Electrician", 
     "Doors & Windows", "Paving Exterminator", "Concrete", "Insulation" ,"Painter", "Transport","Dentist", "Lawyer", "Home Inspection", "Tools","Cabinets""Disposal", 
     "Designer", "Training", "Welder", "Well Drilling", "Fence", "Machine Shop", "Lighting", "Glass", "Hydraulic equipment", "Printer", "Water Softener", "Clinic",
     "Boxes", "Marketing", "Bookkeeping", "Signs", "Medical Supplies", "Fireplace", "Car Aesthetic", "Ceramic", "Repair Household Items", "Real Estate", "Cloth", "Container","Crane rental",
     "Tank Cleaning", "Security", "Restaurant Equipment", "Room Rental", "Sauna", "Property Management", "Sleeping Disorders", "Watch Store", "Sport", "Warehouse", "Tent Rental",
     "Tire store", "Towing", "Film Maker", "Alarm Systems", "Land Surveyor", "Portable Toilet - Rental", "Irrigation", "Car Battery", "Car Painting", "Car Shop", "Car Wash", "Casino",
     "Chiropractor", "Commercial Fire Sprinklers", "Framing Store", "Insurance","Kennel", "Pools", "Animal Clinic","Lock", "Manufacturing", "Microelectronics", "Natural Gas Dealer",
     "Trophy Builder", "Packaging", "Party", "Pompes", "Wood "]
    )



    
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
     if lower_bound<0:
         lower_bound = 0
     upper_bound = mean_prediction + np.std(tree_predictions) * 0.25 

        # Display results
     st.success(f"Predicted Conversions: {mean_prediction:.2f}")
     st.write(f"Prediction Interval: [{lower_bound:.2f}, {upper_bound:.2f}]")
   

    
     
    




