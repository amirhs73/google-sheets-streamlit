import streamlit as st
import pandas as pd
import pickle
import numpy as np
import joblib
import os
import gdown



logo = "images.png"
st.image(logo, width = 200)

st.title("Google Ads Predictor")





download_url = "https://drive.google.com/uc?id=1ZzDxojj59la2ahxLtvv3UPpXbbBkKZX-"
# Download the model
model_file = "random_forest_model_conversions.pkl"

if not os.path.exists(model_file):
    with st.spinner("Downloading the model..."):
        gdown.download(download_url, model_file, quiet=False)

# Load the Random Forest model
with open(model_file, "rb") as file:
    model3 = joblib.load("random_forest_model_conversions.pkl")




option = st.selectbox(
    "What would you like to do?",
    (
        "Select an option",
        "1. New Sale Predictions",
        "2. Top Keywords Analysis by Industry"
    ),
)

# Option 1: View Dataset Summary
if option == "1. New Sale Predictions":
    def load_model():
     model_path1 = "random_forest_model.pkl"
     with open(model_path1, "rb") as file:
        model = joblib.load("random_forest_model.pkl")
     return model
    model = load_model()
    def load_model2():
     model_path2 = "random_forest_model_campaign.pkl"
     with open(model_path2, "rb") as file:
        model2 = joblib.load("random_forest_model_campaign.pkl")
     return model2
    model2 = load_model2()
    st.header("1. New Sale Predictions")
    st.write("Enter the values for the following inputs to predict the outcome:")
    

    # Take input from the user
    #clicks2 = st.number_input("Number of Clicks", min_value=0)
    #avg_cpc = st.number_input("Average Cost Per Click", min_value=0.0, format="%.2f")
    
    Cost = st.number_input("How much do they want to spend per month?", min_value=0)

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
    
    input_data = pd.DataFrame({
            "Season_encoded": [numeric_season],
            "Location ID": [numeric_location],
            "Industry_encoded": [numeric_industry],
        })
    input_data2 = pd.DataFrame({
            "Season_encoded": [numeric_season],
            "Location ID": [numeric_location],
            "Industry_encoded": [numeric_industry],
            "Cost": [Cost],
        })
    if st.button("Calculate"):
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
     #st.success(f"Predicted CPC for the whole account: {mean_prediction:.2f}")
     #st.write(f"The predicted CPC is between [{lower_bound:.2f}] and [{upper_bound:.2f}]")
     predicted_conversions3 = model2.predict(input_data)
      # Get individual tree predictions
     tree_predictions2 = np.array([tree.predict(input_data)[0] for tree in model2.estimators_])
        
        # Calculate the mean prediction
     mean_prediction2 = np.mean(tree_predictions2)

        # Calculate the prediction interval
     lower_bound2 = mean_prediction2 - np.std(tree_predictions2) * 0.25  # Approx. 95% confidence
     if lower_bound2<0:
         lower_bound2 = 0
     upper_bound2 = mean_prediction2 + np.std(tree_predictions2) * 0.25 
     upper_pr_clicks = Cost*0.675/lower_bound2
     lower_pr_clicks = Cost*0.675/upper_bound2
        # Display results
     #st.success(f"Predicted CPC for search campaigns: {mean_prediction2:.2f}")
     st.write(f"The predicted CPC for the search campaigns is between {lower_bound2:.2f} and {upper_bound2:.2f}")
     st.write(f"They could have between {round(lower_pr_clicks)} and {round(upper_pr_clicks)} number of clicks for this budget")
        
     predicted_conversions4 = model3.predict(input_data2)
      # Get individual tree predictions
     tree_predictions3 = np.array([tree.predict(input_data2)[0] for tree in model3.estimators_])
        
        # Calculate the mean prediction
     mean_prediction3 = np.mean(tree_predictions3)

        # Calculate the prediction interval
     lower_bound3 = mean_prediction3 - np.std(tree_predictions3) * 0.25  # Approx. 95% confidence
     if lower_bound3<0:
         lower_bound3 = 0
     upper_bound3 = mean_prediction3 + np.std(tree_predictions3) * 0.25 

        # Display results
     #st.success(f"Predicted Conversions: {mean_prediction3:.2f}")
     st.write(f"The predicted conversions is between {round(lower_bound3)} and {round(upper_bound3)}")
     


if option == "2. Top Keywords Analysis by Industry":
    conversion_weight = 10
    st.title("Top Keywords Analysis by Industry")
    file_path = "Keyword_analysis.csv"
    data2 = pd.read_csv(file_path)
    data2['Score'] = data2['Conversions'] * conversion_weight + data2['Clicks']
        
    industry_options = sorted(data2['Industry'].unique())
    selected_industry = st.selectbox("Select your industry:", industry_options)
    if selected_industry:
            # Filter data for the selected industry
            industry_data = data2[data2['Industry'] == selected_industry]
            
            # Find top keywords (sorted by score)
            top_keywords = industry_data.sort_values(by='Score', ascending=False).head(5)
            
            # Display top keywords
            st.header(f"Top Keywords for {selected_industry}")
            st.dataframe(top_keywords[['Keyword', 'Clicks', 'Conversions', 'Score']])
