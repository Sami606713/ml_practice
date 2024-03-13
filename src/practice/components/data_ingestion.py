from src.practice.logger import logging
from src.practice.exception import CustomException
import pandas as pd
import os,sys
from dataclasses import dataclass
from src.practice.utils import read_data
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    raw_data_path=os.path.join('data','raw_data.csv')
    test_data_path=os.path.join('data','test_data.csv')
    train_data_path=os.path.join('data','train_data.csv')


class DataIngestion:
    def __init__(self):
        self.data_ingestion=DataIngestionConfig()
    
    def Inisiate_DataIgestion(self):
        try:
            logging.info("Reading the data")
            data=read_data()

            logging.info('making the dir')
            os.makedirs(os.path.dirname(self.data_ingestion.raw_data_path),exist_ok=True)
            
            logging.info('saving the raw data')
            data.to_csv(self.data_ingestion.raw_data_path,index=False,header=True)

            logging.info("splitting the data")
            train_data,test_data=train_test_split(data,test_size=0.2,random_state=42)

            logging.info('saving the test and train data')
            train_data.to_csv(self.data_ingestion.train_data_path,index=False,header=True)
            test_data.to_csv(self.data_ingestion.test_data_path,index=False,header=True)
            
            return (
                self.data_ingestion.test_data_path,
                self.data_ingestion.train_data_path
                )

            
        except Exception as se:
            raise CustomException(se,sys)
    


