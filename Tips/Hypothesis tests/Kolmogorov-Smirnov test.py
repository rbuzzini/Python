# Kolmogorov-Smirnov test is a generalization of Shapiro-Wilk test.
# It is used:
# - to compare the distribution of a sample with the distribution of a known population
# - to compare the distribution of a sample with the distribution of another sample
# H0: the sample has been created from the known distribution (or the two samples
# have been created from the same distribution)

import numpy as np
from scipy.stats import *

np.random.seed(0)
x = np.random.normal(size=200)
z = np.random.uniform(size=300)


# 1sample-KS test
kstest(x, norm.cdf) # the statistics is calculated on the cumulative distribution functions
# here we are testing if x has been generated from a normal distribution
# p-value=0.62 ==> we don't reject the null hypothesis
kstest(z, norm.cdf)
# p-value~=0 ==> as we could except we reject the null hypothesis

# Note:
# be careful in the usage of this test because its statistic is very sensible 
# to the distribution tails and in some cases it aproximates to much its value.


#2sample-KS test
ks_2samp(x, z)
# p-value=0 ==> we reject the null hypothesis, x and z aren't generated from the same distribution
y = np.random.normal(size=100)
ks_2samp(x, y)
# p-value=0.84 ==> we don't reject the null hypothesis

# This test is very useful to assess that training and test datasets variables
# have statistically the same distribution
# If the probability distribution is different between training and test set
# we could change the random.seed of the function that split the dataset into
# training and test in order to change the sample datasets until we have 
# similar datasets.
