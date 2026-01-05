# End-To-End Mental Health Prediction

A comprehensive machine learning pipeline that predicts whether a person may require mental health treatment based on survey responses. The project includes data processing, model training, evaluation, and deployment through a Flask web application.

---

## Features

• **Complete ML Pipeline** - From data ingestion to deployment  
• **Data Validation & Transformation** - Robust data processing components  
• **Multi-Algorithm Comparison** - Compare multiple machine learning models  
• **Real-Time Predictions** - Flask web interface with instant results  
• **Configuration Management** - YAML-based flexible configuration system  
• **Modular Architecture** - Easily extensible and maintainable codebase  

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Sujal1035-tech/End-To-End-Mental-Health-Prediction.git
cd End-To-End-Mental-Health-Prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```

---

##  Usage

###  Train the Model
```bash
python main.py
```

### Access Web Interface
```bash
python app.py
```
---

##  Project Structure

```
End-To-End-Mental-Health-Prediction/
│
├──  config/                 # Configuration files
│   ├──  config.yaml
│   ├──  params.yaml
│   └──  schema.yaml
│
├──  artifacts/              # Generated model artifacts
│
├── src/mlProject/         # Source code
│   ├──  components/        # Pipeline components
│   ├──  pipeline/          # Training pipelines
│   ├──  utils/             # Utility functions
│   └──  config/            # Configuration management
│
├──  templates/             # HTML templates
├──  static/                # CSS and static files
├──  app.py                 # Flask web application
├──  main.py                # Training pipeline
└──  requirements.txt       # Dependencies
```

---

## Pipeline Components

| **Stage** | **Description** |
|-----------|-----------------|
| **1️⃣ Data Ingestion** | Loads and processes mental health survey data |
| **2️⃣ Data Validation** | Schema validation and quality checks |
| **3️⃣ Data Transformation** | Feature engineering and preprocessing |
| **4️⃣ Model Training** | Multiple algorithms with hyperparameter tuning |
| **5️⃣ Model Evaluation** | Performance metrics and comparison |
| **6️⃣ Model Deployment** | Flask web application with prediction API |

---

## Configuration

| **File** | **Purpose** |
|----------|-------------|
|  `config.yaml` | Data sources and pipeline settings |
|  `params.yaml` | Model hyperparameters |
|  `schema.yaml` | Data validation rules |

## 🤖 Model Performance

The project implements and compares multiple algorithms:

| **Algorithm** | **Type** |
|---------------|----------|
|  **Logistic Regression** | Linear Classifier |
|  **K-Nearest Neighbors** | Instance-based |
|  **Decision Tree** | Tree-based |
|  **Random Forest** | Ensemble Method |
|  **Support Vector Machine** | Kernel-based |
|  **Naive Bayes** | Probabilistic |
|  **XGBoost** | Gradient Boosting |
|  **CatBoost** | Gradient Boosting |
|  **LightGBM** | Gradient Boosting |

###  Best Model Results

** Best Performing Model: Random Forest Classifier**

**Model Performance:**

| **Metric** | **Score** |
|------------|-----------|
|  **Accuracy** | 84.86% |
|  **F1-Score** | 85.71% |
|  **Precision (Yes)** | 82.01% |
|  **Recall (Yes)** | 89.76% |
|  **Precision (No)** | 88.39% |
|  **Recall (No)** | 79.84% |

###  Detailed Classification Report

```
                precision    recall   f1-score   support
           No       0.88      0.80      0.84       124
          Yes       0.82      0.90      0.86       127
    
     accuracy                           0.85       251
    macro avg       0.85      0.85      0.85       251
 weighted avg       0.85      0.85      0.85       251
```

 **All performance metrics are generated during training and stored in the artifacts directory.**

---

##  Contributing

We welcome contributions! Here's how:

1. ** Fork** the repository
2. ** Create** a feature branch
3. ** Make** your changes
4. ** Submit** a pull request

---

##  License

This project is licensed under the **MIT License**.

---

##  Contact

** Sujal** - [GitHub Profile](https://github.com/Sujal1035-tech)


⭐ **If you find this project helpful, please give it a star!** ⭐

