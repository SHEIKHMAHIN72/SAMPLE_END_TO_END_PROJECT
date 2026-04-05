
import os
import sys
from src.mlops_project.logger import logging
from src.mlops_project.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("SQL_HOST")
user = os.getenv("SQL_USER")
password = os.getenv("SQL_PASSWORD")
database = os.getenv("SQL_DATABASE")

def read_sql_data():
    logging.info("reading data from sql database")
    try:

        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        logging.info(f"connection established succesfully: {mydb}")
        df = pd.read_sql("SELECT * FROM student", mydb)
        print(df.head())

        return df
    

    except Exception as ex:
        raise CustomException(ex, sys)   
