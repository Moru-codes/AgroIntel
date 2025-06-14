# agrointel_app.py

import streamlit as st
import numpy as np
import joblib

# Load model and encoder
model = joblib.load("agrointel_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.title("🌾 AgroIntel Crop Recommendation System")
st.write("Enter the soil and weather conditions to get the best crop recommendation.")

# Input fields
N = st.slider("Nitrogen (N)", 0, 140, 50)
P = st.slider("Phosphorus (P)", 5, 145, 50)
K = st.slider("Potassium (K)", 5, 205, 50)
temperature = st.slider("Temperature (°C)", 10.0, 45.0, 25.0)
humidity = st.slider("Humidity (%)", 10.0, 100.0, 60.0)
ph = st.slider("pH Level", 3.0, 10.0, 6.5)
rainfall = st.slider("Rainfall (mm)", 20.0, 300.0, 100.0)





# Prediction button
if st.button("Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    crop = label_encoder.inverse_transform(prediction)[0]
    st.success(f"✅ Recommended Crop: **{crop.capitalize()}**")
