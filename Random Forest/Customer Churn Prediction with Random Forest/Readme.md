# 📞 Customer Churn Prediction using Ensemble Machine Learning

## 📋 Project Overview
This project aims to predict customer churn for subscription-based businesses using various classification algorithms. By leveraging ensemble learning techniques like Random Forest, XGBoost, CatBoost, and Stacking Classifiers, the model helps businesses identify at-risk customers based on their demographics and service usage patterns.

## 📊 Problem Statement
Customer churn is a major challenge for telecom, internet service providers, and SaaS businesses. Predicting which customers are likely to leave allows companies to proactively engage them with targeted offers and improved services. The goal is to build a robust machine learning model that can predict churn based on customer behavior and demographic attributes.

## 📂 Dataset
The project uses the popular Telco Customer Churn dataset.

-   **Source:** [Telco Customer Churn on Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
-   **Format:** CSV

#### Key Features:
-   `tenure` (in months)
-   `MonthlyCharges`
-   `TotalCharges`
-   `Partner` (Yes/No)
-   `Dependents` (Yes/No)
-   `PhoneService` (Yes/No)
-   `PaperlessBilling` (Yes/No)

## ⚙️ Models Trained & Evaluated
Several classification models were trained, with the Stacking Ensemble model providing the highest accuracy.

| Model                    | Accuracy (%) |
| ------------------------ | ------------ |
| Logistic Regression      | 78.6         |
| Random Forest Classifier | 79.1         |
| XGBoost Classifier       | 77.7         |
| CatBoost Classifier      | 78.6         |
| **Stacking Ensemble** | **79.3** |

## 📈 Visualizations
The analysis includes several key visualizations to evaluate model performance and derive insights.

-   **Confusion Matrix:** Shows the number of correct and incorrect predictions (True Positives, False Positives, etc.).
-   **ROC Curve:** Evaluates the model’s ability to differentiate between churning and non-churning customers.
-   **Precision-Recall Curve:** Particularly useful for evaluating performance on an imbalanced dataset like churn prediction.
-   **Feature Importance Plot:** Highlights which features most influence a customer's decision to churn.

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/Arsalan80425/Machine-Learning-Projects.git](https://github.com/Arsalan80425/Machine-Learning-Projects.git)
```

### 2. Install Dependencies
It's recommended to use a virtual environment. Install all required libraries:
```bash
pip install pandas numpy scikit-learn xgboost catboost matplotlib seaborn streamlit
```

### 3. Run the Analysis
Open and run the Jupyter Notebook (`.ipynb` file) to see the model training process, evaluations, and visualizations.

### 4. Launch the Web App
To run the interactive web application, use the following command in your terminal:
```bash
streamlit run app.py
```

## 🚧 Future Improvements
-   Incorporate more business-relevant features, such as the number of customer support calls or service upgrades/downgrades.
-   Deploy the final model as a live API endpoint for real-time predictions.
-   Enhance the web app to allow dynamic feature input and display individual churn probability scores.

## 📬 Contact
For any queries or collaboration opportunities, please reach out at: [arsalanshaikh0408@gmail.com](mailto:arsalanshaikh0408@gmail.com)