
# 🧠 End-To-End Mental Health Prediction

This repository contains an end-to-end machine learning pipeline designed to predict whether a person may require mental health treatment based on survey responses. The project includes all core stages of an ML workflow: data ingestion, validation, transformation, model training, evaluation, and deployment through a Flask web application.


##  🚀 Project Pipeline

```mermaid
graph LR
A[Data Ingestion] -->] B[Data Validation]
B --> C[Data Transformation]
C --> D[Model Training]
D --> E[Model Evaluation]
E --> F[Model Deployment]


### 📁 Project Structure

End-To-End-Mental-Health-Prediction/
│
├── config/
│   ├── config.yaml
│   ├── params.yaml
│   └── schema.yaml
│
├── artifacts/
│
├── src/mlProject/
│   ├── components/
│   ├── pipeline/
│   ├── utils/
│   └── config/
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
