from src.kidneyDiseaseClassifier import logger
from src.kidneyDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.kidneyDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.kidneyDiseaseClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.kidneyDiseaseClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Training"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_eval = EvaluationPipeline()
    model_eval.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e