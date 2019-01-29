import pandas as pd

# load data and tidy headers
data = pd.read_excel('Bristol Data.xlsx', index_col = 0).dropna(axis = 0)
data.columns = data.columns.str.lower()

info_cols = ['msoa', 'lad', 'lad_nm', 'reg', 'pop']

lsoa_info = data[info_cols]

lsoa_data = data.loc[:, ~data.columns.isin(info_cols)]