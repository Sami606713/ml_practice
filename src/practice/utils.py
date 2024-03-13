from src.practice.logger import logging
from src.practice.exception import CustomException
import pandas as pd
import os,sys,pymysql
from dotenv import load_dotenv
load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')

def read_data():
    try:
        logging.info("setting the database connection")
        conn=pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )
        data=pd.read_sql_query("select * from exams",conn)
        print(data.head())

        return data
    except Exception as e:
        raise CustomException(e,sys)
