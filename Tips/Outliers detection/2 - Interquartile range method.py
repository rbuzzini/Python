import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes

# The interquartile range method is at the basis of Box-Plot representation.
# Value < (Q1 - 1.5*IQR) or Value > (Q3 + 1.5*IQR) where IQR = (Q3-Q1) and
# Q3 = 75% percentile and Q1 = 25% percentile.

# Setting random seed
np.random.seed(0)

# Pseudo-random dataset
x = np.random.lognormal(size=1000, sigma=1.0)
df = pd.DataFrame({'x': x})

# Define quantiles and IQR:
q1, q3 = np.quantile(x, [0.25, 0.75])
iqr = q3-q1

# Outliers flag column:
df['outlier_iqr'] = (x < q1-1.5*iqr) | (x > q3+1.5*iqr)

df.sort_values(by='outlier_iqr', ascending=False)

# This method is the most used in outlier detection analysis.