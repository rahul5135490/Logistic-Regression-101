# app2.py
import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load('logistic_model.pkl')

st.title("🌸 Iris Setosa Classifier")

# User Input Fields
sepal_length = st.number_input("Sepal Length", min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.number_input("Sepal Width", min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.number_input("Petal Length", min_value=0.0, max_value=10.0, value=1.4)
petal_width = st.number_input("Petal Width", min_value=0.0, max_value=10.0, value=0.2)

if st.button("🔍 Predict"):
    input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_features)

    if prediction[0] == 1:
        st.success("✅ Ye Iris Setosa hai!")
    else:
        st.error("❌ Ye Iris Setosa nahi hai.")
