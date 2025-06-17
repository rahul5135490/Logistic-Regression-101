import streamlit as st
import numpy as np
import joblib

# Model load karo
model = joblib.load('concrete_strength_model.pkl')

st.title("🧱 Concrete Strength Predictor")

st.markdown("Enter the following input values to predict the compressive strength of concrete:")

# User input fields
col1, col2 = st.columns(2)

with col1:
    cement = st.number_input("Cement (kg in m³)", min_value=0.0, value=141.3)
    slag = st.number_input("Slag", min_value=0.0, value=212.0)
    ash = st.number_input("Ash", min_value=0.0, value=0.0)
    water = st.number_input("Water", min_value=0.0, value=203.5)

with col2:
    superplastic = st.number_input("Superplasticizer", min_value=0.0, value=0.0)
    coarseagg = st.number_input("Coarse Aggregate", min_value=0.0, value=971.8)
    fineagg = st.number_input("Fine Aggregate", min_value=0.0, value=748.5)
    age = st.number_input("Age (in days)", min_value=0.0, value=28.0)

# Predict button
if st.button("🔍 Predict Strength"):
    input_data = np.array([[cement, slag, ash, water, superplastic, coarseagg, fineagg, age]])
    prediction = model.predict(input_data)
st.success(f"Predicted Concrete Strength: {float(prediction[0]):.2f} MPa")

