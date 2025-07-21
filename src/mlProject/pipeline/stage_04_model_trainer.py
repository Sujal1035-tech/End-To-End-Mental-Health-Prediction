from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()  # corrected name
        model_trainer = ModelTrainer(config=model_trainer_config)  # corrected object name
        model_trainer.train_and_evaluate()  # corrected method call
