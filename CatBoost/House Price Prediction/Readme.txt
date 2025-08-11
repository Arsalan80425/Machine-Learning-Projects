# 🏡 House Price Prediction using Advanced Ensemble Learning

## 📋 Project Overview
This project aims to predict the sale price of houses using various regression algorithms. By leveraging ensemble learning techniques like Random Forest, XGBoost, LightGBM, CatBoost, and Stacking Regressors, the model achieves high accuracy in predicting housing prices based on features like area size, number of rooms, garage capacity, and year built.

## 📊 Problem Statement
Accurate house price prediction is crucial for real estate agents, buyers, and sellers to make informed decisions. The goal is to build a robust machine learning model that can predict the sale price of a house given its structural and historical attributes.

## 📂 Dataset
The dataset used for this project contains various features of residential homes.

#### Key Features:
-   **Format:** CSV
-   Lot Area (sq ft)
-   Number of Full & Half Bathrooms
-   Number of Bedrooms
-   Number of Kitchens
-   Total Rooms
-   Car Garage Capacity
-   Basement Presence & Height
-   Year Built

## ⚙️ Models Trained & Evaluated
Multiple regression models were trained and evaluated. The Stacking Ensemble model, which combines the strengths of multiple models, achieved the best performance.

| Model                   | R² Score | MAE (₹) | RMSE (₹) |
| ----------------------- | -------- | ------- | -------- |
| Linear Regression       | 0.73     | 31,902  | 46,375   |
| Ridge Regression        | 0.73     | 31,902  | 46,375   |
| Lasso Regression        | 0.74     | 31,736  | 45,886   |
| Random Forest Regressor | 0.80     | 24,998  | 39,712   |
| XGBoost Regressor       | 0.80     | 25,009  | 40,162   |
| LightGBM Regressor      | 0.81     | 24,916  | 38,622   |
| CatBoost Regressor      | 0.82     | 24,537  | 38,144   |
| **Stacking Ensemble** | **0.82** | **24,266** | **37,957** |


## 📈 Visualizations
Several visualizations were created to analyze the model's performance and understand the data.

-   **Actual vs Predicted Prices Scatter Plot:** Shows how close predictions are to actual prices.
-   **Residual Plot:** Checks for random distribution of errors, indicating a good model fit.
-   **Feature Importance Plot:** Highlights which features impact the sale price the most (derived from the LightGBM model).
-   **Distribution of Prediction Errors:** Verifies that the model's errors are normally distributed.

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/Arsalan80425/Machine-Learning-Projects.git](https://github.com/Arsalan80425/Machine-Learning-Projects.git)
```

### 2. Install Dependencies
It's recommended to use a virtual environment. Install all required libraries:
```bash
pip install pandas numpy scikit-learn xgboost lightgbm catboost matplotlib streamlit
```

### 3. Run the Analysis
Open and run the Jupyter Notebook (`.ipynb` file) to see the model training process, evaluations, and visualizations.

### 4. Launch the Web App
To run the interactive web application, use the following command in your terminal:
```bash
streamlit run app.py
```

## 🚧 Future Improvements
-   Add more real-world features like location-based data (e.g., crime rate, school ratings).
-   Deploy the final model as an API endpoint for easier integration.
-   Enable dynamic feature selection by the user in the web app.

## 📬 Contact
For any queries or collaboration opportunities, please reach out at: [arsalanshaikh0408@gmail.com](mailto:arsalanshaikh0408@gmail.com)
