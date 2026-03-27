import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("heart_model.pkl", "rb"))

st.title("Heart Disease Prediction")

age = st.number_input("Age")
chol = st.number_input("Cholesterol")
bp = st.number_input("Blood Pressure")
thalach = st.number_input("Max Heart Rate")

if st.button("Predict"):
    
    data = np.array([[age, chol, bp, thalach]])
    
    result = model.predict(data)

    if result[0] == 1:
        st.error("Heart Disease Risk")
    else:
        st.success("No Heart Disease")