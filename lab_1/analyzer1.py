import pandas as pd

def get_data(file_name):

    df = pd.read_csv(file_name,  skipinitialspace=True)
    first_two_columns = df[['Country', 'Population']]

    thirt_four_columns = df[['Births', 'Deaths']]

    return [first_two_columns, thirt_four_columns]

