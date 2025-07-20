from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline


STAGE_NAME = "Data_Ingestion_stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} start<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed >>>>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Data_Validation_Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} start<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed >>>>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e  # re-raising the exception to propagate it to the caller

