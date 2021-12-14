# You can use pandas crosstab method to compute a simple cross tabulation 
# of two (or more) factors. By default computes a frequency table of the 
# factors unless an array of values and an aggregation function are passed.

import pandas as pd
import numpy as np

# Create two arrays which relationship could be interesting.
# They could have been two categorical features of a pandas df. 
weight_size = np.array(['heavy', 'light', 'medium', 'heavy', 'light', 'light'])
height_size = np.array(['tall', 'tall', 'short', 'short', 'short', 'short'])

pd.crosstab(weight_size, height_size)

