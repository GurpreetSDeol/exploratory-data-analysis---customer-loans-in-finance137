import yaml
from sqlalchemy import create_engine
from sqlalchemy import exc
import pandas as pd
import os
from pathlib import Path

def load_credentials():
    with open('C:\\Users\\Gurpr\\OneDrive\\Documents\\AI Core\\Exploratory Data Analysis - Customer Loans in Finance\\credentials.yaml') as file:
        credentials_data = yaml.safe_load(file)
    return credentials_data


class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.host = credentials.get('RDS_HOST')
        self.port = credentials.get('RDS_PORT')
        self.user = credentials.get('RDS_USER')
        self.password = credentials.get('RDS_PASSWORD')
        self.database = credentials.get('RDS_DATABASE')
     
    def initialize_sql_engine(self):
        engine = create_engine(
            f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")
        engine.connect()
        return engine
    

    def extract_data_as_dataframe(self, table):
       
        engine = self.initialize_sql_engine()
        df = pd.read_sql_table(table, engine)
        
        return df
    
    @staticmethod
    def save_data_to_csv( df, name, folder='C:\\Users\\Gurpr\\OneDrive\\Documents\\AI Core\\Exploratory Data Analysis - Customer Loans in Finance\\Data'):
        pwd = os.getcwd()
        save_path = os.path.join(pwd, folder, name)
        filepath = Path(save_path)
        df.to_csv(filepath, index=False)

  


def load_data_from_csv(file_path):
    df = pd.read_csv(file_path)
    return df


# Load credentials from YAML file
credentials_data = load_credentials()

# Create an instance of RDSDatabaseConnector
rds_connector = RDSDatabaseConnector(credentials_data)

df_from_rds = rds_connector.extract_data_as_dataframe('loan_payments')

rds_connector.save_data_to_csv(df_from_rds, 'output_loan_data.csv')

# Load DataFrame from CSV
#loaded_df = load_data_from_csv('Data\output_loan_data.csv')
#print(loaded_df.head())
