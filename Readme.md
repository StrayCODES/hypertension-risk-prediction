# Hypertension Risk Prediction

This project predicts the risk of hypertension using machine learning models trained on a healthcare dataset. The solution is deployed as an interactive [Streamlit](https://streamlit.io/) web app for easy access and use by healthcare professionals and individuals.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [How It Works](#how-it-works)
- [Model Performance](#model-performance)
- [Interventions & Recommendations](#interventions--recommendations)
- [How to Run Locally](#how-to-run-locally)
- [Streamlit App](#streamlit-app)
- [Requirements](#requirements)
- [Acknowledgements](#acknowledgements)

---

## Overview

Hypertension (high blood pressure) is a major risk factor for cardiovascular diseases. Early identification of individuals at risk enables timely intervention and improved health outcomes. This project uses a binary classification model to predict whether a person is at risk of developing hypertension based on various health and lifestyle features.

---

## Features

- **Interactive Streamlit Web App** for risk prediction
- Data exploration and visualization
- Multiple machine learning models (Logistic Regression, Random Forest, XGBoost, CatBoost)
- Feature importance and explainability (SHAP)
- Recommendations for risk reduction

---

## Dataset

The dataset includes the following features:

- Age
- BMI
- Salt Intake
- Stress Score
- BP History
- Exercise Level
- Medication
- Smoking Status
- Family History
- Has_Hypertension (target)

_Source: [Kaggle - Hypertension Risk Prediction Dataset](https://www.kaggle.com/datasets/miadul/hypertension-risk-prediction-dataset)_

---

## How It Works

1. **Data Preprocessing:**  
   - Handle missing values  
   - Encode categorical variables  
   - Feature engineering

2. **Model Training:**  
   - Train/test split  
   - Multiple classifiers evaluated  
   - Best model selected (CatBoost)

3. **Model Evaluation:**  
   - Accuracy, ROC-AUC, classification report  
   - Feature importance and SHAP explainability

4. **Deployment:**  
   - Model saved with `joblib`  
   - Streamlit app for user input and prediction

---

## Model Performance

- **CatBoost Classifier** achieved the best performance.
- Evaluation metrics (on test set):
  - Accuracy: ~0.85 (example)
  - ROC-AUC: ~0.90 (example)
- Feature importance and SHAP plots included in the notebook.

---

## Interventions & Recommendations

Based on model findings, the following interventions are recommended for individuals at risk:

- **Lifestyle Programs:** Encourage weight management, reduced salt intake, and increased physical activity.
- **Stress Management:** Provide stress reduction resources.
- **Smoking Cessation:** Offer support for quitting smoking.
- **Regular Screening:** Especially for those with family history or high-risk profiles.
- **Medication Review:** Ensure adherence and effectiveness for those on medication.

---

## How to Run Locally

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/hypertension-risk-prediction.git
    cd hypertension-risk-prediction
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app:**
    ```sh
    streamlit run app.py
    ```

4. **Open your browser:**  
   Visit `http://localhost:8501` to use the app.

---

## Streamlit App

The Streamlit app allows users to:

- Enter health and lifestyle information
- Get instant hypertension risk prediction
- View model explanations and recommendations

---

## Requirements

- Python 3.8+
- pandas, numpy, scikit-learn, seaborn, matplotlib
- xgboost, catboost, shap, joblib
- streamlit

Install all dependencies with:
```sh
pip install -r requirements.txt