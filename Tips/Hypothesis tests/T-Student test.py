# Import packages
import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt



# Generate a normal distributed sample
np.random.seed(0)
x = np.random.normal(size=200)
plt.hist(x)
plt.show()

x.mean() # 0.07



# How much our sample mean differs from 0?
# H0: sample mean = 0 (2 tails test)
# To answer this question we use the 1-sample T-Student test:
ttest_1samp(x, 0)
# p-value = 0.32 => we don't reject the null hypothesis
ttest_1samp(x, 10)
# p-value ~=0 => we reject the null hypothesis

# 1 tail tests:
ttest_1samp(x, 10, alternative='less')



# 2-samples T-Student test:

y = np.random.normal(size=100)
y.mean()
# We want to establish if mean of y is statistically different from the
# mean of x.
# H0: mean x = mean y
ttest_ind(x, y, equal_var=False)
# p-value is high => we don't reject the null hypothesis
# equal_var is True if the two populations have the same variance 
# (homoskedastics samples). In real life we usually don't have this information
# so I set the parameter to False.



# Reminder: to apply T-Student test there is an important assumption:
# the distribution of the samples on which it is applied must be normal
# To evaluate this assumption you could use Shapiro-Wilk test.

