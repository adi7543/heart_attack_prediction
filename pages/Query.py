import streamlit as st
import joblib
import numpy as np
import json

# Load the trained model
model = joblib.load("model.pkl")

st.title("Heart Disease Risk Prediction")

# Input fields (you can customize layout)
Age = st.number_input("Age", 1, 100, 54)
Sex_Male = st.radio("Sex", ["Female", "Male"]) == "Male"
Cholestrol = st.number_input("Cholestrol", 100, 1000, 297)
Diet = st.selectbox("Diet Quality", ["Unhealthy", "Healthy"]) == "Healthy"
Heart_Rate = st.slider("Heart Rate", 50, 150, 75)
Diabetes = st.checkbox("Diabetes")
Family_History = st.checkbox("Family History")
Smoking = st.checkbox("Smoking")
Obesity = st.checkbox("Obesity")
Alcohol = st.checkbox("Alcohol Consumption")
Exercise = st.number_input("Exercise Hours Per Week", 0.0, 20.0, 0.6)
Previous_Heart_Problems = st.checkbox("Previous Heart Problems")
Medication = st.checkbox("Medication Use")
Stress_Level = st.selectbox("Stress Level (0=Low, 2=High)", [0, 1, 2])
Sedentary = st.number_input("Sedentary Hours Per Day", 0.0, 24.0, 7.79)
# Income = st.number_input("Income", 0, 1000000, 241339)
BMI = st.number_input("BMI", 10.0, 50.0, 20.14)
Triglycerides = st.number_input("Triglycerides", 50, 1000, 795)
Physical_Activity = st.slider("Physical Activity Days Per Week", 0, 7, 5)
Sleep = st.slider("Sleep Hours Per Day", 0, 24, 10)
Systolic = st.number_input("Systolic BP", 80, 200, 172)
Diastolic = st.number_input("Diastolic BP", 50, 130, 86)

# Continent and Country One-Hot
# continent = st.selectbox("Continent", ["Asia", "Australia", "Europe", "North America", "South America"])
# country = st.selectbox("Country", ["Australia", "Brazil", "Canada", "China", "Colombia", "France", "Germany", "India", "Italy",
#                                    "Japan", "New Zealand", "Nigeria", "South Africa", "South Korea", "Spain", "Thailand",
#                                    "United Kingdom", "United States", "Vietnam"])

# Convert inputs into a single dictionary
data = {
    "Age": Age,
    "Sex_Male": int(Sex_Male),
    "Cholestrol": Cholestrol,
    "Diet": int(Diet),
    "Heart Rate": Heart_Rate,
    "Diabetes": int(Diabetes),
    "Family History ": int(Family_History),
    "Smoking ": int(Smoking),
    "Obesity": int(Obesity),
    "Alcohol Consumption": int(Alcohol),
    "Exercise Hours Per Week": Exercise,
    "Previous Heart Problems": int(Previous_Heart_Problems),
    "Medication Use": int(Medication),
    "Stress Level": Stress_Level,
    "Sedentary Hours Per Day": Sedentary,
    # "Income": Income,
    "BMI": BMI,
    "Triglycerides": Triglycerides,
    "Physical Activity Days Per Week": Physical_Activity,
    "Sleep Hours Per Day": Sleep,
    "Systolic": Systolic,
    "Diastolic": Diastolic,
    # "Continent_Asia": int(continent == "Asia"),
    # "Continent_Australia": int(continent == "Australia"),
    # "Continent_Europe": int(continent == "Europe"),
    # "Continent_North America": int(continent == "North America"),
    # "Continent_South America": int(continent == "South America"),
    # "Hemisphere_Southern Hemisphere": 0,  # Optional logic here if needed
}

# One-hot encode country
# all_countries = ["Australia", "Brazil", "Canada", "China", "Colombia", "France", "Germany", "India", "Italy", "Japan",
#                  "New Zealand", "Nigeria", "South Africa", "South Korea", "Spain", "Thailand", "United Kingdom", "United States", "Vietnam"]
# for c in all_countries:
#     data[f"Country_{c}"] = int(country == c)

if st.button("Predict"):
    input_array = np.array([data[key] for key in sorted(data.keys())]).reshape(1, -1)
    result = model.predict(input_array)
    st.success(f"Prediction: {result[0]}")
