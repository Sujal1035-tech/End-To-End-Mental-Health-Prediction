# End-To-End Mental Health Prediction

A machine learning pipeline that predicts whether a person may require mental health treatment based on survey responses. The project includes data processing, model training, evaluation, and deployment through a Flask web application.

## Features

- Complete ML pipeline from data ingestion to deployment
- Data validation and transformation components
- Multiple machine learning algorithms comparison
- Flask web interface for real-time predictions
- YAML-based configuration system
- Modular and extensible architecture

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sujal1035-tech/End-To-End-Mental-Health-Prediction.git
   cd End-To-End-Mental-Health-Prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

## Usage

### Train the Model
```bash
python main.py
```

### Access Web Interface
```bash
python app.py
```
Open `http://localhost:5000` in your browser.

## Project Structure

```
End-To-End-Mental-Health-Prediction/
├── config/                    # Configuration files
│   ├── config.yaml
│   ├── params.yaml
│   └── schema.yaml
├── artifacts/                 # Generated model artifacts
├── src/mlProject/            # Source code
│   ├── components/           # Pipeline components
│   ├── pipeline/            # Training pipelines
│   ├── utils/               # Utility functions
│   └── config/              # Configuration management
├── templates/               # HTML templates
├── static/                  # CSS and static files
├── app.py                   # Flask web application
├── main.py                  # Training pipeline
└── requirements.txt         # Dependencies
```

## Pipeline Components

1. **Data Ingestion** - Loads and processes mental health survey data
2. **Data Validation** - Schema validation and quality checks
3. **Data Transformation** - Feature engineering and preprocessing
4. **Model Training** - Multiple algorithms with hyperparameter tuning
5. **Model Evaluation** - Performance metrics and comparison
6. **Model Deployment** - Flask web application with prediction API

## Configuration

- `config.yaml` - Data sources and pipeline settings
- `params.yaml` - Model hyperparameters
- `schema.yaml` - Data validation rules

## Web Application

The Flask app provides:
- Interactive survey form for mental health assessment
- Real-time prediction results
- User-friendly interface with educational resources

## Model Performance

The project implements and compares:
- Random Forest Classifier
- Logistic Regression
- Support Vector Machine
- Gradient Boosting

Performance metrics are generated during training and stored in the artifacts directory.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Contact

**Sujal** - [GitHub Profile](https://github.com/Sujal1035-tech)

---

**Disclaimer**: This tool is for educational purposes only and should not replace professional medical advice.
