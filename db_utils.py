import yaml
from sqlalchemy import create_engine


def load_credentials(file_path='credentials.yaml'):

     with open(file_path, 'r') as file:
            credentials_data = yaml.safe_load(file)
            return credentials_data



class RDSDatabaseConnector:


    def __init__(self, credentials):
        self.host = credentials.get('host', '')
        self.port = credentials.get('port', 3306)
        self.user = credentials.get('user', '')
        self.password = credentials.get('password', '')
        self.database = credentials.get('database', '')


    def initilise_sql_engine(self): 
    
  
        engine = create_engine(
            f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}",
            pool_recycle=3600
        )


    def extract_data_as_dataframe(self, query):
    
           
        df = pd.read_sql_query(query, self.engine)
        return df

    
    def save_data_to_csv(self, df, file_path):
       
        df.to_csv(file_path, index=False)