import streamlit as st 
import joblib 
import numpy as np 
 
# Load model and scaler 
model = joblib.load("heart_model.pkl") 
scaler = joblib.load("scaler.pkl") 
 
st.title("❤� Heart Disease Risk Predictor") 
 
# Input fields 
age = st.number_input("Age", 20, 100, 45) 
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1]) 
cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3]) 
trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120) 
chol = st.number_input("Cholesterol", 100, 600, 200) 
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1]) 
restecg = st.selectbox("Resting ECG (0–2)", [0, 1, 2]) 
thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150) 
exang = st.selectbox("Exercise Induced Angina", [0, 1]) 
oldpeak = st.number_input("ST depression", 0.0, 6.0, 1.0) 
slope = st.selectbox("Slope of ST", [0, 1, 2]) 
ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3]) 
thal = st.selectbox("Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible)", [0, 1, 2, 3]) 
 
if st.button("Predict"): 
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, 
thalach, 
                            exang, oldpeak, slope, ca, thal]]) 
    input_scaled = scaler.transform(input_data) 
    prediction = model.predict(input_scaled) 
 
    if prediction[0] == 1: 
        st.error("⚠� High risk of heart disease!") 
    else: 
        st.success("✅ Low risk of heart disease.") 