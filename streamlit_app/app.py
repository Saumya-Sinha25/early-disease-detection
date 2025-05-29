import streamlit as st
import requests

st.set_page_config(page_title="Disease Detector", layout="centered")

st.title("🧬 Early Disease Detection")
st.markdown("Enter your health info to predict diabetes risk.")

# Input form
glucose = st.slider("Glucose", 50, 200, 100)
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
age = st.slider("Age", 10, 100, 30)
dpf = st.slider("Diabetes Pedigree Function", 0.1, 2.5, 0.5)
risk_score = round((glucose * bmi) / 100, 2)

if st.button("Predict"):
    input_data = {
        "Glucose": glucose / 200,  # Assuming your model is trained on scaled data
        "BMI": bmi / 50,
        "Age": age / 100,
        "DiabetesPedigreeFunction": dpf / 2.5,
        "risk_score": risk_score / 100
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=input_data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: **{result['status']}**")
    else:
        st.error("Error: Could not get prediction from API.")
