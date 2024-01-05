import pandas as pd
import numpy as np 
from DataFormat import DataFormat
from Plotter import Plotter
from scipy import stats

class DataFrameTransform:

    def __init__(self, df):
        self.df = df

    #These are different methods pf handling null columnues: 1) replacing them with 0, 
    # 2) using the mean of non null vlaues for that column, 
    # 3) uisng the median of the non null columnues for that column, 
    # 4) dropping mull rows

  
   
    def impute_with_zero(self, columns ):
        for column in columns :
            self.df[column] = self.df[column].fillna(0)
    
 
    def impute_with_mean(self, columns):
        for column in columns :
            self.df[column] = self.df[column].fillna(self.df[column].mean())
  
  
    def impute_with_median(self, columns ):
        for column in columns :
            self.df[column] = self.df[column].fillna(self.df[column].median())

   
    def drop_null_rows(self, columns ):
          self.df.dropna(subset=columns , inplace=True)

    
    def log_transform(self, columns ):
        for column in columns :
            self.df[column] = self.df[column].map(lambda x: np.log(x) if x > 0 else 0)


    def box_cox_transform(self, columns):
        for column in columns:
            transformed_column = self.df[column] + 0.01
            a, b = stats.boxcox(transformed_column)
            self.df[column] = a
