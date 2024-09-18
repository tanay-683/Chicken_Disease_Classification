# this will be my entrypoint
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>Starting {STAGE_NAME}<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>Ending {STAGE_NAME}<<<<<<<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e) 
    raise e


    
