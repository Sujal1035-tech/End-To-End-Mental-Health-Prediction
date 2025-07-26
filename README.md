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

## 🚀 Installation And How Run
```bash
# 1. Clone
git clone https://github.com/Sujal1035-tech/End-To-End-Mental-Health-Prediction.git
cd End-To-End-Mental-Health-Prediction

# 2. Install deps
pip install -r requirements.txt

# 3. Run the full pipeline
python main.py          # Trains & saves model + artifacts

# 4. Launch the web app
python app.py           # Open http://localhost:5000
