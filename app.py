import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("heart_model.pkl", "rb"))

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

st.title("❤️ Heart Disease Risk Prediction")
st.write("Enter patient medical details")

# Layout (2 columns)
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 1, 100, 25)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", [0,1,2,3])
    trestbps = st.slider("Resting Blood Pressure", 80, 200, 120)
    chol = st.slider("Cholesterol", 100, 400, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120", [0,1])

with col2:
    restecg = st.selectbox("Rest ECG", [0,1,2])
    thalach = st.slider("Max Heart Rate", 60, 220, 150)
    exang = st.selectbox("Exercise Induced Angina", [0,1])
    oldpeak = st.slider("Oldpeak", 0.0, 6.0, 1.0)
    slope = st.selectbox("Slope", [0,1,2])
    ca = st.selectbox("Number of Major Vessels", [0,1,2,3])
    thal = st.selectbox("Thal", [0,1,2,3])

# Convert categorical values
sex = 1 if sex == "Male" else 0

# Prediction
if st.button("Predict Risk"):

    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    st.subheader("Result")

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

    st.write(f"**Risk Probability:** {round(probability[0][1]*100,2)} %")
