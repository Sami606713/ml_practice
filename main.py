from src.practice.logger import logging
from src.practice.exception import CustomException
import sys
from src.practice.utils import read_data
from src.practice.components.data_ingestion import DataIngestionConfig
from src.practice.components.data_ingestion import DataIngestion


if __name__=="__main__":
    logging.info("start..")
    try:
        logging.info("inside the try block")
        data=DataIngestion()
        data.Inisiate_DataIgestion()
    except Exception as e:
        raise CustomException(e,sys)