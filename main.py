from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

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

STAGE_NAME = "Data_Transformation_Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} start<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed >>>>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e  # re-raising the exception to propagate it to the caller

STAGE_NAME = "Model_Training_Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} start<<<<<<")
    model_training = ModelTrainerPipeline()
    model_training.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed >>>>>>>\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e  # re-raising the exception to propagate it to the caller

STAGE_NAME = "Model_Evaluation_Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} start<<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed >>>>>>>\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e  # re-raising the exception to propagate it to the caller

