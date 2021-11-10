import pandas as pd

# Supposed we have a dataframe with our items value sold in each month, where
# each month is a column.
#  

df = pd.DataFrame({
    'item': ['phone', 'mouse', 'keyboard'],
    'January 2021': [1000, 200, 300],
    'February 2021': [3500, 100, 250],
    'March 2021': [2000, 400, 500],
    'April 2021': [5000, 50, 150]})

df

# to do this we can use pandas melt method:
df_long = pd.melt(df, id_vars='item', var_name='MonthYear', value_name='ValueSold')
# where:
#   id_vars=variable which need to be unaltered
#   var_name is the new column name
#   value_name is the name of the column that contains var_name values 

df_long


# Bonus: how we can extract month number and year from MonthYear column?
from time import strptime

df_long['month'] = df_long['MonthYear'].apply(lambda x: x.split(' ')[0])
df_long['year'] = df_long['MonthYear'].apply(lambda x: x.split(' ')[1])
df_long['MonthNum'] = df_long['month'].apply(lambda x: strptime(x, '%B').tm_mon)

#Month-Year index:
df_long['day'] = 1
df_long.set_index(pd.to_datetime(df_long['MonthNum'].astype(str)+"-"+df_long['year'].astype(str)).dt.to_period('M'), inplace=True)
df_long.index
df_long['2021-01':'2021-02']