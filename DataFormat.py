import pandas as pd
from db_utils import RDSDatabaseConnector


class DataFormat:

    def __init__(self, df):
        self.df = df

    def strings_to_dates(self, columns):
        for column in columns :
            self.df[column] = pd.to_datetime(self.df[column], format="%b-%Y")
   
    def values_to_categories(self, columns):
        for column in columns :
            self.df[column] = self.df[column].astype('category')

    
    def string_to_boolean(self, column_name):
        x = {'n': False, 'y': True}
        self.df[column_name].map(x)
        self.df[column_name] = self.df[column_name].astype('bool')
        print(self.df[column_name].unique())


    def drop_columns (self, columns):
        for column in columns :
            self.df.drop(column, axis=1, inplace=True)

    def round_float(self, column, decimal_places):
        self.df[column] = self.df[column].apply(lambda x: round(x, decimal_places))

   

