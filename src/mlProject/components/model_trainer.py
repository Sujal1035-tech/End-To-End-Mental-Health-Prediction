import os
import joblib
import pandas as pd
import importlib
from sklearn.metrics import accuracy_score, classification_report, f1_score
from dataclasses import dataclass
from typing import Dict, Any
from mlProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def load_data(self):
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        X_train = train_df.drop("treatment", axis=1)
        y_train = train_df["treatment"]

        X_test = test_df.drop("treatment", axis=1)
        y_test = test_df["treatment"]

        return X_train, X_test, y_train, y_test

    def load_scaler(self):
        return joblib.load(self.config.scaler_path)

    def train_and_evaluate(self):
        X_train, X_test, y_train, y_test = self.load_data()
        scaler = self.load_scaler()

        X_train_scaled = scaler.transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        best_model = None
        best_f1 = 0
        best_model_name = ""

        print(f"\n📊 Evaluating models...\n")

        for model_name, model_config in self.config.models.items():
            print(f"🔹 Training: {model_name.replace('_', ' ').title()}")

            module = importlib.import_module(model_config['module'])
            model_class = getattr(module, model_config['class'])
            model = model_class(**model_config.get('params', {}))

            model.fit(X_train_scaled, y_train)
            y_pred = model.predict(X_test_scaled)

            acc = accuracy_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred, pos_label=1)

            print(f"✅ Accuracy: {acc:.4f} | F1 Score: {f1:.4f}")
            print("📄 Classification Report:")
            print(classification_report(y_test, y_pred, target_names=["No", "Yes"]))

            if f1 > best_f1:
                best_f1 = f1
                best_model = model
                best_model_name = model_name

        # Save the best model using joblib
        print(f"\n💾 Saving best model: {best_model_name.title()} (F1: {best_f1:.4f})")
        os.makedirs(os.path.dirname(self.config.model_dir), exist_ok=True)
        joblib.dump(best_model, self.config.model_dir)
