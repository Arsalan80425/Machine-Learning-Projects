import streamlit as st
import numpy as np
import joblib

# Loading Models
lr_model = joblib.load('lr_model.pkl')
rf_model = joblib.load('rf_model.pkl')
xgb_model = joblib.load('xgb_model.pkl')
cat_model = joblib.load('cat_model.pkl')
stack_model = joblib.load('stack_model.pkl')

# Loading Scaler
scaler = joblib.load('scaler.pkl')

# Model Accuracies (Manual Entries from Evaluation Results)
model_accuracies = {
    'Logistic Regression': 78.0,
    'Random Forest': 79.5,
    'XGBoost': 77.8,
    'CatBoost': 78.6,
    'Stacked Ensemble': 79.3
}

# Page Layout
st.set_page_config(layout="wide")

# Sidebar for Model Selection & Accuracies
with st.sidebar:
    
    # Model Selection Dropdown
    model_choice = st.selectbox(
        "Select Model to Predict",
        list(model_accuracies.keys())
    )

    st.markdown("### Model Accuracies")
    for model, acc in model_accuracies.items():
        st.write(f"**{model}:** {acc}%")


# Main Title & Disclaimer
st.title("Customer Churn Prediction App")
st.markdown("""
<div style='font-size: 16px; color: grey;'>
⚠️ <b>Disclaimer:</b> This is a demo project for predictive modeling. Accuracy may vary depending on data and feature selection.
</div>
""", unsafe_allow_html=True)

# User Inputs
st.header("Enter Customer Details:")

col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure (in months)", min_value=0, max_value=100, value=1, step=1)
    total_charges = st.number_input("Total Charges", min_value=0.0, value=10.0)
    phone_service = st.selectbox("Has Phone Service?", ['No', 'Yes'])

with col2:
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=10.0)
    partner = st.selectbox("Has Partner?", ['No', 'Yes'])
    dependents = st.selectbox("Has Dependents?", ['No', 'Yes'])

# 7th Feature
paperless_billing = st.selectbox("Uses Paperless Billing?", ['No', 'Yes'])

# Encode Binary Features
partner = 1 if partner == 'Yes' else 0
dependents = 1 if dependents == 'Yes' else 0
phone_service = 1 if phone_service == 'Yes' else 0
paperless_billing = 1 if paperless_billing == 'Yes' else 0

# Predict Button
if st.button("Predict Churn"):
    # Numerical Data Scaling
    numerical_data = np.array([[tenure, monthly_charges, total_charges]])
    numerical_data_scaled = scaler.transform(numerical_data)

    # Combining Scaled Numerical Data with Binary Features
    input_data = np.concatenate((numerical_data_scaled, [[partner, dependents, phone_service, paperless_billing]]), axis=1)

    # Model Prediction
    if model_choice == 'Logistic Regression':
        prediction = lr_model.predict(input_data)[0]
    elif model_choice == 'Random Forest':
        prediction = rf_model.predict(input_data)[0]
    elif model_choice == 'XGBoost':
        prediction = xgb_model.predict(input_data)[0]
    elif model_choice == 'CatBoost':
        prediction = cat_model.predict(input_data)[0]
    else:
        prediction = stack_model.predict(input_data)[0]

    # Display Result
    if prediction == 1:
        st.error("⚠️ This customer is likely to CHURN!")
    else:
        st.success("✅ This customer is NOT likely to churn.")
