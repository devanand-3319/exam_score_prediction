import streamlit as st
import pandas as pd
import pickle

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open("exam_scores.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Exam Score Prediction")

st.title("Exam Score Prediction")

studyhr = st.number_input("Study Hours Per Day", value=4.05)
attendance = st.number_input("Attendance Percentage", value=85.36)
previous = st.number_input("Previous Score", value=42.47)
sleephr = st.number_input("Sleep Hours", value=5.70)
prtest = st.number_input("Practice Tests Taken", value=2)
internet = st.number_input("Internet Access", value=1)

if st.button("Predict"):
    input_data = pd.DataFrame(
        [[studyhr, attendance, previous, sleephr, prtest, internet]],
        columns=[
            "StudyHoursPerDay",
            "AttendancePercentage",
            "PreviousScore",
            "SleepHours",
            "PracticeTestsTaken",
            "InternetAccess"
        ]
    )

    prediction = model.predict(input_data)
    st.subheader(f"Predicted Score: {prediction[0]:.2f}")
