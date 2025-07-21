# mlProject/entity/config_entity.py
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict,Any

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    drop_columns: List[str]
    columns_to_fillna: Dict[str, str]
    columns_to_drop_due_to_missing: List[str]
    top_features: int
    scaler_path: Path
    processed_train_data_path: Path
    processed_test_data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    scaler_path: Path
    model_dir: Path
    models: Dict[str, Dict[str, Any]]
