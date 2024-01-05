from db_utils import load_data_from_csv
from tabulate import tabulate


class DataFrameInfo:
    def __init__(self, df):
        self.df = df

    
    def describe_column(self):
        return self.df.dtypes

   
    def extract_statistics(self, column):
        for column in columns:
            print(f"Statistics for column :{val}")
            return self.df[val].describe()
    
    
    def distinct_values(self, columns ):
        unique_values = {}
        for column in columns :
            print(f"Unique values for val: {val} \n")
            unique_values[val] = self.df[val].nunique()
        return unique_values
   
   
    def get_shape(self):
        print("Dataframe Shape:")
        return self.df.shape


    def null_percentage(self):
        null_percentages = (self.df.isna().sum() * 100 /
                            len(self.df)).to_frame(name="% Null")
        non_zero_null_percentages = null_percentages[null_percentages["% Null"] > 0]
        return non_zero_null_percentages

    
    
    def data_skew(self, columns):
        skew_data = []
        for column in columns:
            skew_value = self.df[column].skew()
            skew_data.append([column, skew_value])

        print(tabulate(skew_data))

