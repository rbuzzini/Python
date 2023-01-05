# Levene's test is used to evaluate the statistical significance of the difference
# between the variance of two samples.
# Null Hypothesis: the two samples have the same variance (are homoskedastics).

# The most used test to evaluate if two samples have the same variance is Fisher's
# test (test F), although this test is strongly dependent from the assumption of
# the normality of the two samples on which it is applied.
# Instead Levene's test allows us to compare the two samples variance remaining
# robust on the NON-Normality of these samples.

# Levene's test can be used with more than two samples.

import pandas as pd
import numpy as np
from scipy.stats import *

x = np.random.normal(size=200)
y = np.random.normal(size=100)


levene(x, y)   # we don't reject the null hypothesis of equal variance
x.var(), y.var()

z = np.random.uniform(size=300)
levene(x, z)   # we reject the null hypothesis

levene(x, y, z)   # we reject the null hypothesis

# Important:
# levene method has a parameter named 'center', this parameter indicates the
# value on which the residues are calculated. It is equal to 'median' by default,
# this allows it to be robust on samples non normality