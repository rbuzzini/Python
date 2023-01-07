import pandas as pd
import numpy as np

# Z-score calculates how many standard deviations a point is away from the mean.
# It works better with a symmetric distribution.
# I suggest not to use this score on asymmetric distribution (in this case IQR
# method is better).

# Set the seed to generate always the same pseudo-random numbers.
np.random.seed(0)

x = np.random.lognormal(size=1000, sigma=0.3)

# Create Pandas dataframe
df = pd.DataFrame({'x': x})

# Z-score column (as we know it is a distance indicator):
df['distanza'] = np.abs((x-x.mean()))/x.std()

# The greater the distance the greater the probability that the observation
# is an outlier.