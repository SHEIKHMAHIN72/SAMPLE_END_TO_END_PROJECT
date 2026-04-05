from src.mlops_project.logger import logging
from src.mlops_project.exception import CustomException
import sys
from src.mlops_project.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    logging.info("starting point of the application")
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
                
    except Exception as e:
        logging.info("custom exception occured")
        raise CustomException(e, sys)

