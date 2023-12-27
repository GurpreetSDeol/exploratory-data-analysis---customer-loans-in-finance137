import pandas as pd
import numpy as np 

class DataFrameTransform:

    def __init__(self, df):
        self.df = df

    #These are different methods pf handling null values: 1) replacing them with 0, 
    # 2) using the mean of non null vlaues for that column, 
    # 3) uisng the median of the non null values for that column, 
    # 4) dropping mull rows

  
    def fill_zero(self, vals):
        for val in vals:
            self.df[val] = self.df[val].fillna(0)
    
 
    
    def fill_mean(self, vals):
        for val in vals:
            self.df[val] = self.df[val].fillna(self.df[val].mean())
  
  
    def fill_median(self, vals):
        for val in vals:
            self.df[val] = self.df[val].fillna(self.df[val].median())

   
    def drop_null_rows(self, cols):