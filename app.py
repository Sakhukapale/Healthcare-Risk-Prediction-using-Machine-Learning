import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("heart_model.pkl", "rb"))

st.title("Heart Disease Prediction")

# All 13 inputs
age = st.number_input("Age")
sex = st.selectbox("Sex", [0,1])
cp = st.selectbox("Chest Pain", [0,1,2,3])
trestbps = st.number_input("BP")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("FBS >120", [0,1])
restecg = st.selectbox("Rest ECG", [0,1,2])
thalach = st.number_input("Max HR")
exang = st.selectbox("Exercise Angina", [0,1])
oldpeak = st.number_input("Oldpeak")
slope = st.selectbox("Slope", [0,1,2])
ca = st.selectbox("CA", [0,1,2,3])
thal = st.selectbox("Thal", [0,1,2,3])

if st.button("Predict"):

    data = np.array([[age, sex, cp, trestbps, chol, fbs,
                      restecg, thalach, exang, oldpeak,
                      slope, ca, thal]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("High Risk")
    else:
        st.success("Low Risk")
