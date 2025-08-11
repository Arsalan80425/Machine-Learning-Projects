import streamlit as st
import numpy as np
import pickle

# Load All Models
@st.cache_resource
def load_models():
    models = {}
    model_files = {
        'Linear Regression': 'linear_model.pkl',
        'Ridge Regression': 'ridge_model.pkl',
        'Lasso Regression': 'lasso_model.pkl',
        'XGBoost': 'xgb_model.pkl',
        'Random Forest': 'rf_model.pkl',
        'LightGBM': 'lightgbm_model.pkl',
        'CatBoost': 'catboost_model.pkl',
        'Stacking Ensemble': 'stack_model.pkl'
    }
    for name, file in model_files.items():
        with open(file, 'rb') as f:
            models[name] = pickle.load(f)
    return models

models = load_models()

# Model Accuracies (Update with your actual values)
model_accuracies = {
    'Linear Regression': 0.68,
    'Ridge Regression': 0.67,
    'Lasso Regression': 0.68,
    'XGBoost': 0.75,
    'Random Forest': 0.77,
    'LightGBM': 0.78,
    'CatBoost': 0.78,
    'Stacking Ensemble': 0.77
}



# Title and Ames Dataset Info
st.title("🏡 House Price Prediction App")
st.subheader("📍 Based on Ames Housing Dataset (Iowa, USA)")
st.caption("This prediction is tailored for properties in Ames, Iowa as per historical housing data.")

# Sidebar: Model Selection
st.sidebar.header("Model Selection")
model_choice = st.sidebar.selectbox("Select Model", list(models.keys()))

# Sidebar: Model Accuracies (Always Visible)
st.sidebar.markdown("### Model Accuracies (R² Score)")
for model_name, score in model_accuracies.items():
    st.sidebar.markdown(f"**{model_name}:** {score * 100:.0f}%")

# Feature Inputs (Compact Layout)
st.header("Enter House Details:")

col1, col2 = st.columns(2)
with col1:
    lot_area = st.number_input("Lot Area (sq ft)", min_value=500, max_value=50000, step=100)
with col2:
    bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=10)

col3, col4 = st.columns(2)
with col3:
    full_bath = st.number_input("Full Bathrooms", min_value=0, max_value=5)
with col4:
    half_bath = st.number_input("Half Bathrooms", min_value=0, max_value=5)

col5, col6 = st.columns(2)
with col5:
    kitchen = st.number_input("Kitchens", min_value=1, max_value=5)
with col6:
    total_rooms = st.number_input("Total Rooms", min_value=1, max_value=20)

col7, col8 = st.columns(2)
with col7:
    car_garage = st.selectbox("Car Garage Capacity", [0, 1, 2, 3, 4])
with col8:
    basement = st.selectbox("Basement Present?", [0, 1])

# Feature Engineering
total_bathrooms = full_bath + 0.5 * half_bath
rooms_per_area = total_rooms / lot_area

# Prepare Input Data (10 Features)
input_data = np.array([[lot_area, full_bath, half_bath, bedrooms, kitchen, total_rooms,
                        car_garage, basement, total_bathrooms, rooms_per_area]])

# Prediction
if st.button("Predict Price"):
    model = models[model_choice]
    prediction_usd = model.predict(input_data)[0]
    st.success(f"Estimated House Price: ${prediction_usd:,.2f}")



# Disclaimer
st.markdown("---")
st.caption("⚠️ Disclaimer: This prediction model is based on historical data from Ames, Iowa (USA) and may not generalize accurately to other locations or current market fluctuations.")
