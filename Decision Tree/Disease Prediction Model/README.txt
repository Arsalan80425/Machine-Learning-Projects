# Disease Prediction Using Machine Learning

## Project Description

This project focuses on developing a machine learning model to predict diseases based on a set of symptoms provided by the user. Using various algorithms, the system classifies diseases into one of the 41 categories based on 132 different symptoms. The main goal is to provide a simple yet effective tool for healthcare diagnostics using state-of-the-art machine learning techniques. The models used in this project include **Decision Tree**, **Random Forest**, **XGBClassifier**, **K-Nearest Neighbors (KNN)**, and **Multi-Layer Perceptron (MLP)**.

The project utilizes a dataset, `Augmented_Data.csv`, which contains 132 symptom columns and a target column, "Prognosis", with 41 unique diseases. The final web application, built using **Streamlit**, allows users to input symptoms and receive a predicted diagnosis. 

## Features

- **Symptom Input**: Users can input symptoms to predict possible diseases.
- **Disease Prediction**: Based on the input symptoms, the model predicts the most likely disease.
- **Algorithms Used**: Implements Decision Tree, Random Forest, XGBClassifier, KNN, and MLP for disease classification.
- **Model Evaluation**: Performance metrics like accuracy, precision, recall, and F1-score are used to evaluate model performance.

## Setup Instructions

### Prerequisites

Before setting up the project, ensure that you have the following installed:

- Python 3.x
- pip (Python package installer)
