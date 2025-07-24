# app.py
import streamlit as st
import joblib
import pandas as pd

# Load model and feature columns
model = joblib.load("rf_hypertension_model.pkl")
features = joblib.load("model_features.pkl")

st.title("🩺 Hypertension Risk Prediction")
st.write("Enter the patient's lifestyle & medical details:")
# ...existing code...



# User Inputs
age = st.slider("Age", 18, 100, 30)
salt = st.slider("Daily Salt Intake (g)", 0.0, 20.0, 5.0)
stress = st.slider("Stress Score (0-10)", 0, 10, 5)
sleep = st.slider("Sleep Duration (hours)", 0.0, 12.0, 7.0)
bmi = st.slider("BMI", 10.0, 50.0, 22.0)
family_history = st.selectbox("Family History", ["Yes", "No"])
bp_history = st.selectbox("BP History", ["Normal", "Prehypertension", "Hypertension"])
medication = st.selectbox("Medication", ["None", "Beta Blocker", "Diuretic", "ACE Inhibitor", "Other"])
exercise_level = st.selectbox("Exercise Level", ["Low", "Moderate", "High"])
smoking = st.selectbox("Smoking Status", ["Non-Smoker", "Smoker"])

# Manual encoding (match training logic)
input_dict = {
    'Age': age,
    'Salt_Intake': salt,
    'Stress_Score': stress,
    'Sleep_Duration': sleep,
    'BMI': bmi,
    'Family_History': 1 if family_history == "Yes" else 0,
    'BP_History_Prehypertension': 1 if bp_history == "Prehypertension" else 0,
    'BP_History_Hypertension': 1 if bp_history == "Hypertension" else 0,
    'Medication_Beta Blocker': 1 if medication == "Beta Blocker" else 0,
    'Medication_Diuretic': 1 if medication == "Diuretic" else 0,
    'Medication_ACE Inhibitor': 1 if medication == "ACE Inhibitor" else 0,
    'Medication_Other': 1 if medication == "Other" else 0,
    'Exercise_Level_Low': 1 if exercise_level == "Low" else 0,
    'Exercise_Level_Moderate': 1 if exercise_level == "Moderate" else 0,
    'Smoking_Status_Smoker': 1 if smoking == "Smoker" else 0
}
st.write("""
### Feature Importance Scores


Each feature contributes differently to the model's prediction. The following are the top features and their relative importance (as determined by the model):

- **🩸 Blood Pressure History:**	⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️ (29 points)
- **👪 Family History:**	⭐️⭐️⭐️⭐️ (14 points)
- **🎂 Age:**	⭐️⭐️⭐️⭐️ (13 points)
- **😰 Stress Score:**	⭐️⭐️⭐️⭐️ (11 points)
- **🚬 Smoking:**	⭐️⭐️⭐️⭐️ (11 points)
- **🧂 Salt Intake:**	⭐️⭐️⭐️⭐️ (8 points)
- **💤 Sleep Time:**	⭐️⭐️⭐️ (7 points)
- **⚖️ BMI (Body Size):**	⭐️⭐️⭐️ (7 points)
- **🏃 Exercise Level:**	⭐️ (less than 1 point)
- **💊 Medication Type:**	⭐️ (less than 1 point)


Higher percentages indicate a stronger influence on the prediction. These scores help highlight which factors are most critical in assessing hypertension risk.
""")

# Ensure all features exist
for col in features:
    if col not in input_dict:
        input_dict[col] = 0  # Default value for missing dummies

input_df = pd.DataFrame([input_dict])[features]

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"Prediction: {'Hypertensive' if prediction == 1 else 'Not Hypertensive'}")
