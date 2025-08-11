📞 Customer Churn Prediction using Ensemble Machine Learning
📋 Project Overview
This project aims to predict customer churn for subscription-based businesses using various classification algorithms. By leveraging ensemble learning techniques like Random Forest, XGBoost, CatBoost, and Stacking Classifiers, the model helps businesses identify at-risk customers based on their demographics and service usage patterns.

📊 Problem Statement
Customer churn is a major challenge for telecom, internet service providers, and SaaS businesses. Predicting which customers are likely to leave allows companies to proactively engage them with targeted offers and improved services. The goal is to build a robust machine learning model that can predict churn based on customer behavior and demographic attributes.

📂 Dataset
Source: Telco Customer Churn Dataset

Format: CSV

Key Features:

Tenure (in months)

Monthly Charges

Total Charges

Has Partner (Yes/No)

Has Dependents (Yes/No)

Has Phone Service (Yes/No)

Uses Paperless Billing (Yes/No)

⚙️ Models Trained & Evaluated
Model	Accuracy (%)
Logistic Regression	78.6
Random Forest Classifier	79.1
XGBoost Classifier	77.7
CatBoost Classifier	78.6
Stacking Ensemble	79.3

📈 Visualizations
Graph Insights
Confusion Matrix Shows True Positives, False Positives/Negatives.
ROC Curve Evaluates model’s ability to differentiate classes.
Precision-Recall Curve Useful for imbalanced churn classification.
Feature Importance Plot (Random Forest)	Highlights which features most influence churn.

🚀 Run the Project Locally
Requirements:

Python 3.x

Pandas, Numpy, Scikit-learn

XGBoost, CatBoost

Matplotlib, Seaborn

Streamlit (for the web app)


Run the Jupyter Notebook for model training and visualizations.

To run the Streamlit app: run in terminal "streamlit run app.py"


🚧 Future Improvements
Add more business-relevant features (like Customer Support Calls, Service Upgrades).

Deploy the model as an API endpoint for real-time predictions.

Enable dynamic feature input and display churn probability scores.

📬 Contact
For queries or collaboration, reach out at: arsalanshaikh0408@gmail.com