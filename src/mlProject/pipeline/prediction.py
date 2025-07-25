# prediction.py

import joblib
import numpy as np
import pandas as pd

# Load model and scaler
model = joblib.load("artifacts/model_trainer/model.pkl")
scaler = joblib.load("artifacts/data_transformation/scaler.pkl")

# Top 20 features (replace these with your actual top 20 used in training)
FEATURES = [
    'Age', 'Gender', 'self_employed', 'family_history', 'treatment',
    'work_interfere', 'no_employees', 'remote_work', 'tech_company',
    'benefits', 'care_options', 'wellness_program', 'seek_help',
    'anonymity', 'leave', 'mental_health_consequence',
    'phys_health_consequence', 'coworkers', 'supervisor',
    'mental_vs_physical'
]

# Label Encoding map (must match training time)
label_maps = {
    "Gender": {"male": 0, "female": 1, "other": 2},
    "self_employed": {"No": 0, "Yes": 1},
    "family_history": {"No": 0, "Yes": 1},
    "treatment": {"No": 0, "Yes": 1},
    "work_interfere": {"Never": 0, "Rarely": 1, "Sometimes": 2, "Often": 3, "Do Not Know": 4},
    "no_employees": {"1-5": 0, "6-25": 1, "26-100": 2, "100-500": 3, "500-1000": 4, "More than 1000": 5},
    "remote_work": {"No": 0, "Yes": 1},
    "tech_company": {"No": 0, "Yes": 1},
    "benefits": {"No": 0, "Don't know": 1, "Yes": 2},
    "care_options": {"No": 0, "Not sure": 1, "Yes": 2},
    "wellness_program": {"No": 0, "Don't know": 1, "Yes": 2},
    "seek_help": {"No": 0, "Don't know": 1, "Yes": 2},
    "anonymity": {"No": 0, "Don't know": 1, "Yes": 2},
    "leave": {"Very easy": 0, "Somewhat easy": 1, "Don't know": 2, "Somewhat difficult": 3, "Very difficult": 4},
    "mental_health_consequence": {"No": 0, "Maybe": 1, "Yes": 2},
    "phys_health_consequence": {"No": 0, "Maybe": 1, "Yes": 2},
    "coworkers": {"No": 0, "Some of them": 1, "Yes": 2},
    "supervisor": {"No": 0, "Some of them": 1, "Yes": 2},
    "mental_vs_physical": {"No": 0, "Don't know": 1, "Yes": 2}
}


def preprocess_input(data: dict):
    processed = []
    for feature in FEATURES:
        val = data.get(feature)
        if feature in label_maps:
            processed.append(label_maps[feature][val])
        else:
            processed.append(float(val))  # Age
    return np.array(processed).reshape(1, -1)


def predict(data: dict):
    arr = preprocess_input(data)
    arr_scaled = scaler.transform(arr)
    prediction = model.predict(arr_scaled)[0]
    return "Likely to Seek Mental Health Treatment" if prediction == 1 else "Not Likely to Seek Treatment"
