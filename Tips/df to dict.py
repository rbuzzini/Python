# We can create a pandas datafram from a dictionary, and the reverse
# is possible too. We can do this using to_dict method.

import pandas as pd

df = pd.DataFrame({
    'item': ['phone', 'keyboard', 'mouse'],
    'price': [200, 30, 10]
})

df

# Get a dict whose keys are columns:
df.to_dict()

# Get a list of dicts whose elements are df rows:
df.to_dict(orient='records')