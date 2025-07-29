# covid_dashboard.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -----------------------------
# Simulated Tamil Nadu COVID-19 Data
# -----------------------------
np.random.seed(42)

# Sample dataset
data = {
    'District':np.random.choice([
        "Kanyakumari" , "Madurai"  , "Theni" , "Ramanathapuram" , "Sivagangai" ,
        "Dindugal" , "Thoothukudi" ,"Virudhunagar" , "Tirunelveli" , "Tenkasi"
    ], 300) ,
    'Age': np.random.randint(20, 85, 300),
    'Gender': np.random.choice(['Male', 'Female'], 300),
    'Confirmed': np.random.randint(500, 50000, 300),
    'Deaths': np.random.randint(100, 30000, 300),
    'Recovered': np.random.randint(200, 40000, 300),
    'Active': np.random.randint(50, 15000, 300)
}

df = pd.DataFrame(data)

# -----------------------------
# Streamlit App UI
# -----------------------------
st.title("🦠 𝐓𝐚𝐦𝐢𝐥 𝐍𝐚𝐝𝐮 𝐂𝐎𝐕𝐈𝐃-𝟏𝟗 𝐃𝐚𝐬𝐡𝐛𝐨𝐚𝐫𝐝")

# Sidebar filters
district_filter = st.sidebar.selectbox("Select District" , options= df['District'].unique())
age_range = st.sidebar.slider("Filter by Age", 5, 85, (10, 70))
gender_filter = st.sidebar.selectbox("Select Gender", options=["All", "Male", "Female"])


# Apply filters
filtered_df = df[
    (df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1]) &
    (df['District']==district_filter)
]

if gender_filter != "All":
    filtered_df = filtered_df[filtered_df['Gender'] == gender_filter]

st.markdown(f"**Total Patients Shown:** {len(filtered_df)}")

# -----------------------------
# Dashboard Charts
# -----------------------------

# 1. Confirmed vs Active (Scatter)
st.subheader("📊ᴄᴏɴꜰɪʀᴍᴇᴅ ᴠꜱ ᴀᴄᴛɪᴠᴇ ᴄᴀꜱᴇꜱ")
fig1 = px.scatter(
    filtered_df, x='Confirmed', y='Active', color='District',
    hover_data=['District', 'Age', 'Gender']
)
st.plotly_chart(fig1)

# 2. Confirmed Cases Histogram
st.subheader("📈 ᴅɪꜱᴛʀɪʙᴜᴛɪᴏɴ ᴏꜰ ᴄᴏɴꜰɪʀᴍᴇᴅ ᴄᴀꜱᴇꜱ")
fig2 = px.histogram(
    filtered_df, x='Confirmed', nbins=15, color='Gender',
    title="Confirmed Cases Histogram"
)
st.plotly_chart(fig2)

# 3. Recovered Boxplot by Gender
st.subheader("📦 ʀᴇᴄᴏᴠᴇʀᴇᴅ ᴄᴀꜱᴇꜱ ʙʏ ɢᴇɴᴅᴇʀ")
fig3 = px.box(
    filtered_df, x='Gender', y='Recovered', color='Gender',
    title="Recovered Case Distribution"
)
st.plotly_chart(fig3)

# -----------------------------
# Summary Statistics
# -----------------------------
st.markdown("### 📋 ꜱᴜᴍᴍᴀʀʏ ꜱᴛᴀᴛɪꜱᴛɪᴄꜱ")
st.write(filtered_df[['Confirmed', 'Deaths', 'Recovered', 'Active']].describe())

# -----------------------------
# District with Highest Recoveries
# -----------------------------
st.markdown("### 🏥 ᴅɪꜱᴛʀɪᴄᴛ ᴡɪᴛʜ ʜɪɢʜᴇꜱᴛ ᴛᴏᴛᴀʟ ʀᴇᴄᴏᴠᴇʀᴇᴅ ᴄᴀꜱᴇꜱ")

# Group by district and sum recovered cases
recovered_by_district = df.groupby('District')['Recovered'].sum()

# Find district with max recovered
max_recovered_district = recovered_by_district.idxmax()
max_recovered_value = recovered_by_district.max()

# Display
st.success(f"**{max_recovered_district}** has the highest number of recovered cases : **{max_recovered_value}**")

st.markdown("### 🏥 ᴅɪꜱᴛʀɪᴄᴛ ᴡɪᴛʜ ʟᴏᴡᴇꜱᴛ ᴛᴏᴛᴀʟ ʀᴇᴄᴏᴠᴇʀᴇᴅ ᴄᴀꜱᴇꜱ")

#Find district with min recovered
min_recovered_district = recovered_by_district.idxmin()
min_recovered_value = recovered_by_district.min()

#Display
st.success(f"**{min_recovered_district}** has the lowest number of recovered cases : **{min_recovered_value}**")