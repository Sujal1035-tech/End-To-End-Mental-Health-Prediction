import os
import pandas as pd
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            # ✅ Construct full path to the CSV file
            data_path = os.path.join(self.config.unzip_data_dir, "survey.csv")
            logger.info(f" Reading data from: {data_path}")

            # ✅ Load the data
            data = pd.read_csv(data_path)

            # ✅ Get actual and expected columns
            actual_columns = set(data.columns)
            expected_columns = set(self.config.all_schema.keys())

            # ✅ Compare columns
            missing_in_data = expected_columns - actual_columns
            extra_in_data = actual_columns - expected_columns

            validation_status = True
            if missing_in_data or extra_in_data:
                validation_status = False

            # ✅ Write result to status file
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}\n")
                if missing_in_data:
                    f.write(f"Missing columns in data: {missing_in_data}\n")
                if extra_in_data:
                    f.write(f"Extra columns in data: {extra_in_data}\n")

            logger.info(f"Validation completed. Status: {validation_status}")
            return validation_status

        except Exception as e:
            logger.exception("Exception occurred during validation")
            raise e
