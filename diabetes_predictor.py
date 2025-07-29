import streamlit as st 
import numpy as np
import  joblib

model = joblib.load("diabetes.pkl")
scalar = joblib.load("diabetes_scalar.pkl")

st.title('👩🏻‍⚕️𝐃𝐢𝐚𝐛𝐞𝐭𝐞𝐬 𝐝𝐢𝐬𝐞𝐚𝐬𝐞 𝐩𝐫𝐞𝐝𝐢𝐜𝐭𝐨𝐫')

# inputs
age = st.number_input("𝗔𝗴𝗲 𝗼𝗳 𝘁𝗵𝗲 𝗽𝗮𝘁𝗶𝗲𝗻𝘁 " , 10 , 85 , 35)
glucose = st.number_input("𝗕𝗹𝗼𝗼𝗱 𝘀𝘂𝗴𝗮𝗿 𝗹𝗲𝘃𝗲𝗹" , 0 ,200 ,99)
bp = st.number_input("𝗗𝗶𝗮𝘀𝘁𝗼𝗹𝗶𝗰 𝗽𝗿𝗲𝘀𝘀𝘂𝗿𝗲" , 0 , 130 , 80)
pregnancies = st.number_input("𝗣𝗿𝗲𝗴𝗻𝗮𝗻𝗰𝘆 " , 0 , 20 ,2)
insulin = st.number_input("𝗜𝗻𝘀𝘂𝗹𝗶𝗻 𝗹𝗲𝘃𝗲𝗹" , 0 , 846 ,166)
bmi = st.number_input("𝗕𝗼𝗱𝘆 𝗠𝗮𝘀𝘀 𝗜𝗻𝗱𝗲𝘅" , 0.0 , 70.0 ,24.9)
skinthickness = st.number_input("𝗦𝘂𝗯𝗰𝘂𝘁𝗮𝗻𝗲𝗼𝘂𝘀 𝗳𝗮𝘁 𝘁𝗵𝗶𝗰𝗸𝗻𝗲𝘀s" , 0 , 100 ,20)
diabetes = st.selectbox("𝗜𝘀 𝗮𝗻𝘆𝗼𝗻𝗲 𝗼𝗳 𝘆𝗼𝘂𝗿 𝗳𝗮𝗺𝗶𝗹𝘆 𝗵𝗮𝘀 𝗱𝗶𝗮𝗯𝗲𝘁𝗲𝘀? (𝟬=𝗡𝗼 , 𝟭=𝘆𝗲𝘀)" ,[0,1])

if st.button("𝗣𝗿𝗲𝗱𝗶𝗰𝘁"):
    input_data = np.array([[age , glucose, bp , pregnancies , 
    insulin , bmi , skinthickness , diabetes]])
    input_scaled = scalar.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠� High risk of diabetes disease!") 
    else: 
        st.success("✅ Low risk of diabetes disease.") 