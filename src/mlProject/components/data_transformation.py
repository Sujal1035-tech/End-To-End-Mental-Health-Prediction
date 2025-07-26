import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformationConfig 
import joblib
import logging


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def load_data(self):
        logging.info(f"📄 Loading data from: {self.config.data_path}")
        return pd.read_csv(self.config.data_path)

    def drop_columns(self, df):
        logging.info("🧹 Dropping unnecessary columns")
        cols_to_drop = ["Timestamp", "comments", "state"] if "Timestamp" in df.columns else []
        return df.drop(columns=cols_to_drop, errors='ignore')

    def fill_missing(self, df):
        logging.info("🩹 Filling specific missing values")
        df = df.copy()

        if 'self_employed' in df.columns:
            df['self_employed'] = df['self_employed'].fillna('No')
        if 'work_interfere' in df.columns:
            df['work_interfere'] = df['work_interfere'].fillna('Do Not Know')

        # Optional: log remaining nulls in those columns
        logging.info("🔍 Nulls after filling:\n" + str(df[['self_employed', 'work_interfere']].isnull().sum()))

        return df

    def clean_age(self, df):
        logging.info("🔢 Cleaning Age column")
        df = df.copy()
        df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
        df = df[(df['Age'] >= 10) & (df['Age'] <= 100)]
        return df

    def normalize_gender(self, df):
        logging.info("🚻 Normalizing Gender column")
        df = df.copy()
        df['Gender'] = df['Gender'].astype(str).str.lower().str.strip()

        def clean_gender(val):
            if 'male' in val:
                return 'male'
            elif 'female' in val:
                return 'female'
            else:
                return 'other'

        df['Gender'] = df['Gender'].apply(clean_gender)
        return df

    def reduce_countries(self, df):
        logging.info("🌍 Reducing countries to top 4")
        df = df.copy()
        top_4 = df['Country'].value_counts().nlargest(4).index.tolist()
        df['Country'] = df['Country'].apply(lambda x: x if x in top_4 else 'Other')
        return df

    def encode_features(self, df):
        logging.info("🏷️ Encoding categorical columns")
        df = df.copy()
        le = LabelEncoder()

        cat_cols = df.select_dtypes(include='object').columns.tolist()

        for col in cat_cols:
            df[col] = df[col].astype(str)
            df[col] = le.fit_transform(df[col])
        return df

    def select_features(self, X, y):
        logging.info("✨ Selecting top features")
        selector = SelectKBest(score_func=f_classif, k=self.config.top_features)
        X_new = selector.fit_transform(X, y)
        return X_new, selector.get_support(indices=True)

    def scale_features(self, X):
        logging.info("📏 Scaling features")
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        scaler_dir = os.path.dirname(self.config.scaler_path)
        os.makedirs(scaler_dir, exist_ok=True)
        joblib.dump(scaler, self.config.scaler_path)
        return X_scaled

    def split_and_save(self, X, y):
        logging.info("✂️ Splitting data and saving")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

        train = pd.DataFrame(X_train)
        train['treatment'] = y_train.reset_index(drop=True)
        test = pd.DataFrame(X_test)
        test['treatment'] = y_test.reset_index(drop=True)

        os.makedirs(os.path.dirname(self.config.processed_train_data_path), exist_ok=True)
        os.makedirs(os.path.dirname(self.config.processed_test_data_path), exist_ok=True)

        train.to_csv(self.config.processed_train_data_path, index=False)
        test.to_csv(self.config.processed_test_data_path, index=False)

    def run(self):
        df = self.load_data()
        df = self.drop_columns(df)
        df = self.fill_missing(df)
        df = self.clean_age(df)
        df = self.normalize_gender(df)
        df = self.reduce_countries(df)
        df = self.encode_features(df)

        X = df.drop(columns='treatment')
        y = df['treatment']

        X_selected, selected_indices = self.select_features(X, y)
        X_scaled = self.scale_features(X_selected)
        self.split_and_save(X_scaled, y)
