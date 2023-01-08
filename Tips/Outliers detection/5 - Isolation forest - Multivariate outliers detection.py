# With this method, ad ensemble of trees is built to describe the dataset (
# and to find outliers).
# Outliers to be described require few nodes, while the inliers more.

import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.ensemble import IsolationForest

# Load dataset
X, y = load_diabetes(return_X_y=True)
df2 = pd.DataFrame(X)

# Forest fit and predict on X
forest.fit(X)
forest.predict(X)
# Like for the EllipticEnvelope, IsolationForest returns an array composed by
# 1 and -1.
# 1 = inlier
# -1 = outlier

# Create outlier flag column:
df2['forest_outlier'] = forest.predict(X) == -1

# IsolationForest is more effective than EllipticEnvelope in outliers detection.
# IsoltationForest can be used with great results in historical series too (
# obvoiusly with the right steps).
