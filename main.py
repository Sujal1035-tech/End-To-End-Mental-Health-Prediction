from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data_Ingestion_stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} start<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed >>>>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e 