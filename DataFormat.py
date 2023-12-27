import pandas as pd
from db_utils import RDSDatabaseConnector


class DataFormat:

    def __init__(self, df):
        self.df = df

    def strings_to_dates(self, vals):
        for val in vals:
            self.df[val] = pd.to_datetime(self.df[val], format="%b-%Y")
   
    def values_to_categories(self, vals):
        for val in vals:
            self.df[val] = self.df[val].astype('category')

    
    def string_to_boolean(self, val_name):
        x = {'n': False, 'y': True}
        self.df[val_name].map(x)
        self.df[val_name] = self.df[val_name].astype('bool')
        print(self.df[val_name].unique())


    def drop_vals(self, vals):
        for val in vals:
            self.df.drop(val, axis=1, inplace=True)

    def round_float(self, val, decimal_places):
        self.df[val] = self.df[val].apply(lambda x: round(x, decimal_places))

   
df = pd.read_csv('Data\output_loan_data.csv')
Transformer = DataFormat(df)
 # Convert n and y to bool values
Transformer.string_to_boolean('payment_plan')

categories = ['grade', 'sub_grade', 'home_ownership',
                  'verification_status', 'loan_status', 'purpose', 'employment_length']

Transformer.values_to_categories(categories)

string_dates = ['last_credit_pull_date', 'next_payment_date',
                    'last_payment_date', 'earliest_credit_line', 'issue_date']

TransformedDF = Transformer.df
Transformer.strings_to_dates(string_dates)
print(Transformer.df.dtypes)
print(Transformer.df.info())
RDSDatabaseConnector.save_data_to_csv(TransformedDF, 'Formatted_loan_data.csv')