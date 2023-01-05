import pandas as pd
import numpy as np

# Set the seed to generate always the same pseudo-random numbers.
np.random.seed(0)

x = np.random.lognormal(size=1000, sigma=0.3)

# 1st quantile 5% and the 2nd quantitle 95% (everything outside this treshold
# will be considered as an outlier)

a, b = np.quantile(x, [0.05, 0.95])
print('a = {quantile1}, b = {quantile2}'.format(quantile1=a, quantile2=b))

# Create Pandas dataframe
df = pd.DataFrame({'x': x})

# Add a column to flag the observation is an outlier
df['outlier_percentile'] = (x > b) | (x < a)

# Sort values to have all 'True Flags' at the beginning of the dataset
df.sort_values(by='outlier_percentile', ascending=False)

df.describe()

