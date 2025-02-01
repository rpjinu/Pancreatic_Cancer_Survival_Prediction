import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and encoders
model = joblib.load(r"C:\Users\Ranjan kumar pradhan\.vscode\Best_model.pkl")
label_encoders = joblib.load(r"C:\Users\Ranjan kumar pradhan\.vscode\label_encoders.pkl")

# Verify loaded model type
if not hasattr(model, "predict"):
    st.error("Loaded model is incorrect. Ensure 'Best_model.pkl' contains a trained classifier.")
    st.stop()

# Define feature names
feature_names = [
    "Age", "Gender", "Smoking", "Obesity", "Abdominal_Discomfort", "Back_Pain", 
    "Weight_Loss", "Diabets_Type2", "Stage_at_Diagnosis", "Treatment_Type", 
    "Alcohol_Consumption", "Physical_Activity_Level", "Diet", "Access_to_Healthcare"
]

# Streamlit UI
st.title("Pancreatic Cancer Survival Prediction")
st.write("Enter patient details below:")

# Collect user input
user_input = {}
for feature in feature_names:
    if feature in label_encoders:  # Apply label encoding for categorical values
        options = label_encoders[feature].classes_.tolist()
        user_input[feature] = st.selectbox(f"{feature}", options)
    else:  # Numerical input
        user_input[feature] = st.number_input(f"{feature}", min_value=0, max_value=120, step=1)

# Convert categorical values using label encoders
for feature, value in user_input.items():
    if feature in label_encoders:
        user_input[feature] = label_encoders[feature].transform([value])[0]

# Convert input data to DataFrame
input_data = pd.DataFrame([user_input])

# Predict survival
if st.button("Predict Survival"):
    try:
        prediction = model.predict(input_data)[0]
        result = "Survived" if prediction == 1 else "Did not Survive"
        st.success(f"Prediction: {result}")
    except Exception as e:
        st.error(f"Prediction error: {e}")

st.write("This model uses machine learning to predict survival outcomes based on patient data.")
