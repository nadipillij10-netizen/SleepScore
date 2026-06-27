import streamlit as st
import pandas as pd

st.title("SleepScore – Sleep Quality Predictor")

# Load dataset
data = pd.read_csv("sleep_data.csv")

st.subheader("Enter Your Details")

age = st.number_input("Age", min_value=10, max_value=100, value=25)
sleep_duration = st.number_input("Sleep Duration (hours)", 0.0, 12.0, 7.0)
stress = st.slider("Stress Level (1–10)", 1, 10, 5)
steps = st.number_input("Daily Steps", 0, 20000, 5000)

if st.button("Analyze Sleep"):
    if sleep_duration >= 7 and stress <= 5:
        quality = "Good"
        score = 85
    elif sleep_duration >= 5:
        quality = "Average"
        score = 65
    else:
        quality = "Poor"
        score = 40

    st.success(f"Sleep Quality: {quality}")
    st.write(f"Sleep Score: {score}/100")
