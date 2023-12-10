import yaml
from sqlalchemy import create_engine
import pandas as pd


def load_credentials(file_path):
    with open(file_path, 'r') as file:
        credentials_data = yaml.safe_load(file)
    return credentials_data


class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.host = credentials.get('RDS_HOST')
        self.port = credentials.get('RDS_PORT')
        self.user = credentials.get('RDS_USER')
        self.password = credentials.get('RDS_PASSWORD')
        self.database = credentials.get('RDS_DATABASE')
        self.engine = self.initialize_sql_engine()

    def initialize_sql_engine(self):
        engine = create_engine(
            f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}",
            pool_recycle=3600
        )
        return engine

    def extract_data_as_dataframe(self, query):
        df = pd.read_sql_query(query, self.engine)
        return df

    def save_data_to_csv(self, df, file_path):
        df.to_csv(file_path, index=False)


def load_data_from_csv(file_path):
    df = pd.read_csv(file_path)
    return df


# Load credentials from YAML file
credentials_data = load_credentials('Exploratory Data Analysis - Customer Loans in Finance/credentials.yaml')

# Create an instance of RDSDatabaseConnector
rds_connector = RDSDatabaseConnector(credentials_data)

query = "SELECT * FROM loan_payments"
df_from_rds = rds_connector.extract_data_as_dataframe(query)

rds_connector.save_data_to_csv(df_from_rds, 'output.csv')

# Load DataFrame from CSV
loaded_df = load_data_from_csv('output.csv')
print(loaded_df.head())
