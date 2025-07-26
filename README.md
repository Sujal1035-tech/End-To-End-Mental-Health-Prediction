# 🧠 End-to-End Mental Health Prediction

This project is an end-to-end machine learning pipeline built to predict mental health treatment needs based on user input. It includes data ingestion, validation, transformation, model training, evaluation, and deployment via a Flask web application.

---

## 🚀 Project Pipeline

```mermaid
graph LR
A[Data Ingestion] --> B[Data Validation]
B --> C[Data Transformation]
C --> D[Model Training]
D --> E[Model Evaluation]
E --> F[Flask Deployment]

## Project structure

'''mwemaid
End-To-End-Mental-Health-Prediction/
│
├── config/                   # YAML files for configuration
├── data/                     # Raw and processed data
├── notebooks/                # Jupyter notebooks for EDA and testing
├── artifacts/                # Saved artifacts: model, transformer, scaler
├── src/mlProject/            # Core ML pipeline modules
│   ├── components/           # Data processing & training scripts
│   ├── config/               # Configuration entities
│   ├── pipeline/             # Pipeline stages
│   └── utils/                # Utility functions
├── templates/                # HTML templates for Flask
├── static/                   # CSS styling
├── app.py                    # Flask app
├── main.py                   # Main entry to trigger pipeline
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── setup.py                  # Package info
