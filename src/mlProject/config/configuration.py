# mlProject/config/configuration.py
from mlProject.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from pathlib import Path  # ✅ Correct import


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH
    ):
        # Force convert to Path object in case they are strings
        config_filepath = Path(config_filepath)
        params_filepath = Path(params_filepath)
        schema_filepath = Path(schema_filepath)

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    
    def get_data_transformation_config(self):
        config = self.config.data_transformation
        schema = self.schema

        return DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path),
            drop_columns=schema.get("drop_columns", []),
            columns_to_fillna=schema.get("columns_to_fillna", {}),
            columns_to_drop_due_to_missing=schema.get("columns_to_drop_due_to_missing", []),
            top_features=self.params.data_transformation.top_features,
            scaler_path=Path(config.scaler_path),
            processed_train_data_path=Path(config.processed_train_data_path),
            processed_test_data_path=Path(config.processed_test_data_path)
        )
