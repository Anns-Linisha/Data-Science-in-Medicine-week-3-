import streamlit as st 
import numpy as np
import joblib

model = joblib.load("DIABETIC.PKL")
scalar = joblib.load("DIABETIIC_SCALAR.PKL")

#inputs 
age = st.selectbox("Age of the patient (0=20-30 , 1=30-40 , 2=50-60 , 3=60-70 , 4=70-80 , 5=80-90 , 6=90-100" ,[0,1,2,3,4,5,6] )
gender = st.selectbox("Gender (0=Male , 1=Female)" , [0 ,1])
time_in_hospital = st.selectbox("Time in Hospital (days)" , [1,2,3,4,5,6,7,8,9,10,11,12,13,14])
num_lab_procedures = st.number_input("Number of Lab Procedures" , 1,132,1)
num_procedures = st.number_input("Number of procedures" , 0,6,0)
num_medications = st.number_input("Number of medications " , 1,81,1)
number_diagnoses = st.selectbox("Select number of diagnoses" , [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
a1c_result = st.selectbox("Select A1C result (0=None , 1=Normal , 2=>200 , 3=>300) " , [0,1,2,3])
max_glu_serum = st.selectbox("Select A1C result (1=None , 2=Normal , 3=>200 , 4=>300) " , [0,1,2,3])
insulin = st.selectbox("Select Insulin level (0=No , 1=Steady , 2=Up , 3=Down)", [0,1,2,3])
diabetesMed = st.selectbox("whether you take medicines for diabetes? (1=No , 2=Yes)" , [0,1])
change = st.selectbox("Whether meds were changed during the visit? (0=No , 1=Yes)" , [0,1])


if st.button("Prediction"):
    input_data = np.array([[age , gender , time_in_hospital , num_lab_procedures ,
                            num_procedures , num_medications , number_diagnoses ,
                            a1c_result , max_glu_serum , insulin , diabetesMed , change]])
    input_scaled = scalar.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0]==1:
        st.error("⚠� High risk of readmission!") 
    else: 
        st.success("✅ Low risk of readmission.") 