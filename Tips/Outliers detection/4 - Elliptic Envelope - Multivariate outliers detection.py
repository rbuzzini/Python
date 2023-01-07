# The Elliptic Envelope can be seen as the multivariate version of the Z-score.
# If data are distributed following a multivariate gaussian distribution, the
# Elliptic Envelope builds an ellipsoid which contains almost every point.
# External points are considered outliers.
# This method is very powerful but it has a very strong assumption:
# the data distribution must be a multivariate gaussian.

import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.covariance import EllipticEnvelope

# Load dataset:
X, y = load_diabetes(return_X_y=True)
# We want to detect multivariate outliers in X:

envelope = EllipticEnvelope()
# fit of the EllipticEnvelope:
envelope.fit(X)

df2 = pd.DataFrame(X)

# EllipticEnvelope().predict() returns -1 when the point is an outlier
df2['envelope_outlier'] = envelope.predict(X) == -1

df2.sort_values(by='envelope_outlier', ascending=False)