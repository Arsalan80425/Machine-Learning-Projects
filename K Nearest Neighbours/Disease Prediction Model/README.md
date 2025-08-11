# Disease Prediction Based on Symptoms

This project is a web application that predicts potential diseases based on the symptoms a user provides. It leverages several machine learning models to provide the prediction. The front end is built with Streamlit, making it easy to interact with the models.

## 📋 Features

-   **Interactive Web Interface:** A user-friendly interface built with Streamlit.
-   **Multiple Model Selection:** Allows users to choose from five different trained machine learning models for prediction:
    -   Decision Tree
    -   Random Forest
    -   XGBoost
    -   K-Nearest Neighbors (KNN)
    -   MLP Neural Network
-   **Symptom-Based Prediction:** Users can select multiple symptoms from a comprehensive list to get a disease prediction.
-   **Dynamic Input:** Creates a feature vector based on user selections to feed into the chosen model.

## ⚙️ How It Works

1.  **Select a Model:** The user first chooses one of the available machine learning models from a dropdown menu.
2.  **Select Symptoms:** The user then selects two or more symptoms they are experiencing from a multi-select box.
3.  **Predict:** Upon clicking the "Predict Disease" button, the application converts the selected symptoms into a binary vector.
4.  **Get Result:** This vector is passed to the chosen model, which then outputs the predicted disease.

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Make sure you have Python 3.8 or higher installed on your system.

### 1. Clone the Repository

Clone the main repository to your local machine:

```bash
git clone [https://github.com/Arsalan80425/Machine-Learning-Projects.git](https://github.com/Arsalan80425/Machine-Learning-Projects.git)
```


### 2. Create a Virtual Environment (Recommended)

It's a good practice to create a virtual environment to manage project dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, create one and add the following content:

```
streamlit
pandas
numpy
scikit-learn
xgboost
```

### 4. Place Data and Model Files

Make sure you have the necessary files in your project's root directory:
-   `Augmented_Data.csv` (The dataset used for training)
-   `DecisionTree.joblib`
-   `RandomForest.joblib`
-   `XGBoost.joblib`
-   `KNN.joblib`
-   `MLP.joblib`

### 5. Run the Application

Once the setup is complete, you can run the Streamlit application with the following command:

```bash
streamlit run main.py
```

This will start the application, and you can access it in your web browser at the local URL provided in the terminal (usually `http://localhost:8501`).

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, please feel free to fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
