# Shapiro-Wilk test is used to evaluate the statistic significance between
# the normal and the sample distribution.
# It can be very helpful to evaluate the normal assumption fro the T-Student test.

# H0:the sample has been generated from a normal distribution

import numpy as np
from scipy.stats import *
np.random.seed(0)

# Generate a normal sample:
x = np.random.normal(size=200)
shapiro(x) # ===> as we could expect we don't reject the null hypothesis

z = np.random.uniform(size = 300)
shapiro(z) # ===> as we could expect we reject the null hypothesis

# Note:
# Shapiro-Wilk test has a limit: it doesn't work on big samples (I remember
# that the limit is like 5000 elements. To be sure about this treshhold see
# Python documentation).
# If the sample is to large we can use the Kolmogorov-Smirnov test instead.