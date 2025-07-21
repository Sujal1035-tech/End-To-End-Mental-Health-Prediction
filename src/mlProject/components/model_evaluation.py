import joblib
import pandas as pd
import os, json
from sklearn.metrics import accuracy_score, f1_score, classification_report

class ModelEvaluation:
    def __init__(self, config):
        self.config = config

    def evaluate(self):
        # Load test data
        df = pd.read_csv(self.config.test_data_path)
        X_test = df.drop("treatment", axis=1)
        y_test = df["treatment"]

        # Load scaler ✅
        scaler = joblib.load(self.config.scaler_path)
        X_test_scaled = scaler.transform(X_test)

        # Load model
        model = joblib.load(self.config.model_path)

        # Predict
        y_pred = model.predict(X_test_scaled)  # ✅ scaled test data

        # Metrics
        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, pos_label=1)
        report = classification_report(y_test, y_pred, target_names=["No", "Yes"], output_dict=True)

        # Save metrics
        metrics = {
            "accuracy": acc,
            "f1_score": f1,
            "classification_report": report
        }

        os.makedirs(os.path.dirname(self.config.metric_file_name), exist_ok=True)
        with open(self.config.metric_file_name, "w") as f:
            json.dump(metrics, f, indent=4)

        # Print
        print(f"\n✅ Evaluation Completed:\nAccuracy: {acc:.4f} | F1 Score: {f1:.4f}")
        print("📄 Classification Report:")
        print(classification_report(y_test, y_pred, target_names=["No", "Yes"]))
