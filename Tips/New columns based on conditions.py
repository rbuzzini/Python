import pandas as pd
import numpy as np

df = pd.DataFrame({
    'item': ['phone', 'mouse', 'keyboard'],
    'January 2021': [1000, 200, 300],
    'February 2021': [3500, 100, 250],
    'March 2021': [2000, 400, 500],
    'April 2021': [5000, 50, 150]})

# Make a condition statement on column pandas
df['colour'] = ['white' if x == 'phone' else 'black' for x in df['item']]


# Add a value to an existing field in pandas dataframe after checking conditions:

# Create a new column called based on the value of another column
# np.where assigns True if item price>=400
# Firstly I have to unpivot df
df_long = pd.melt(df, id_vars=['item', 'colour'], var_name='month', value_name='price')
df_long
df_long['high_price?'] = np.where(df_long.price >= 400, True, False)
df_long.head()



# Create a new column based on condition of two columns.
# For example we want to create a "quarter" column only for phones
conditions = [
    df_long['item'].eq('phone') & df_long['month'].isin(['January 2021','February 2021', 'March 2021']),
    df_long['item'].eq('phone') & (df_long['month'] == 'April 2021')
]

choice_list = ['q1','q2']

df_long['quarter'] = np.select(conditions, choice_list)
df_long.head()

# Recap
# python conditionally create new column in pandas dataframe

# If you only have one condition use numpy.where()
# Example usage with np.where:
df_new = pd.DataFrame({'Type':list('ABBC'), 'Set':list('ZZXY')})
print(df_new)

# Add new column based on single condition:
df_new['colour'] = np.where(df_new['Set']=='Z', 'green', 'red')
print(df_new)


# If you have multiple conditions use numpy.select()
# Example usage with np.select:
df_new = pd.DataFrame({'Type':list('ABBC'), 'Set':list('ZZXY')}) # Define df_new
print(df_new)

# Set the conditions for determining values in new column:
conditions = [
    (df_new['Set'] == 'Z') & (df_new['Type'] == 'A'),
    (df_new['Set'] == 'Z') & (df_new['Type'] == 'B'),
    (df_new['Type'] == 'B')]

# Set the new column values in order of the conditions they should
#	correspond to:
choices_list = ['yellow', 'blue', 'purple']

# Add new column based on conditions and choices:
df_new['color'] = np.select(conditions, choices_list, default='black')
print(df_new)


# Source https://www.codegrepper.com/code-examples/python/make+new+column+based+on+condition+pandas