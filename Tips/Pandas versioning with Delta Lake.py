import pandas as pd
from deltalake.writer import write_deltalake
from deltalake import DeltaTable

df = pd.DataFrame({'x': [1, 2]})

# Write df to a delta table 
table = 'delta_lake'
write_deltalake(table, df)

# Append another dataframe to the delta table
df2 = pd.DataFrame({'x': [3, 4]})
write_deltalake(table, df2, mode='append')

DeltaTable(table).to_pandas()

# Read version 0 of the dataset
df_0 = DeltaTable(table, version=0).to_pandas()
df_0

# Read all the data appended until version 1 of the dataframe:
df_1 = DeltaTable(table, version=1).to_pandas()
df_1

# Read df appended in version 1:
df_appended = df_1[~df_1.isin(df_0)].dropna()
df_appended