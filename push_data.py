import os
import json
import sys
from dotenv import load_dotenv
import pandas as pd
import numpy as np
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import pymongo


load_dotenv()
url = os.getenv('MONGO_DB_URL')

import certifi #provides set of root certificates to make secure http connections

ca = certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_to_mongoDB(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(url)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__ == '__main__':
    FILE_PATH  = 'Network_data\phisingData.csv'
    DATABASE = "Project0"
    Collection = "NetworkData"

    netwrokobj = NetworkDataExtract()
    records = netwrokobj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records = netwrokobj.insert_data_to_mongoDB(records, DATABASE, Collection)
    print(no_of_records)
