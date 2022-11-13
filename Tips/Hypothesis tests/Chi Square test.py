# Chi Square test is used to evaluate the statistical significance of the
# difference between the values distribution of a variable related to another
# one in a contingency table.

#H0: the two variables are independent

import pandas as pd
import numpy as np
from scipy.stats import *

# contingency table
tbl = pd.DataFrame(
    np.array([[100, 130], [400, 499]])
    , columns = ['Giovane', 'Anziano']
    , index = ['Alto', 'Basso']
    )

chi2_contingency(tbl)
# - The 1st value is the statistic
# - The 2nd value is the p-value = 0.84 ==> null hypothesis not rejected
# - The 3rd value represents the degree of freedom (row_num - 1) * (col_num - 1)
# - The matrix represents the theoric frequencies if the variables are independent.
# Every theoric frequency is equal to the row_sum * col_sum / total_sum
# The test compare these values with the observed values.