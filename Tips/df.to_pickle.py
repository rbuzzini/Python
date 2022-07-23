# Pickle (serialize) object to file.

# If you have a very large df to use multiple times, you can pickle it in order
# to speed up df readings in the future

import pandas as pd

data = pd.read_csv(r'very large dataframe.csv')

data2 = data.to_pickle(r'path/filename.pkl')

# in the future you can read data2 instead of data, you will speed up the reading