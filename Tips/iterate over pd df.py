import timeit
import time
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 10, size=(100000,4)),
    columns=list('ABCD'))
df.head()

# Experiment results with %timeit

# 1 - Standard python for loop with iloc
def loop_with_for(df):
    temp = 0
    for index in range(len(df)):
        temp += df['A'].iloc[index] + df['B'].iloc[index]
    return temp

print(timeit.timeit(stmt='loop_with_for(df)', setup='from __main__ import loop_with_for, df',number=1))


# 2 - Using pandas iterrows function
def loop_with_iterrows(df):
    temp = 0
    for _, row in df.iterrows():
         temp += row.A + row.B
    return temp
print(timeit.timeit(stmt='loop_with_iterrows(df)', setup='from __main__ import loop_with_iterrows, df',number=1))


# 3 - Using pandas itertuples function
def loop_with_itertuples(df):
    temp = 0
    for row_tuple in df.itertuples():
        temp += row_tuple.A + row_tuple.B
    return temp
print(timeit.timeit(stmt='loop_with_itertuples(df)', setup='from __main__ import loop_with_itertuples, df',number=1))


# 4 - Using python zip
def loop_with_zip(df):
    temp = 0
    for a, b in zip(df['A'], df['B']):
        temp += a + b
    return temp
print(timeit.timeit(stmt='loop_with_zip(df)', setup='from __main__ import loop_with_zip, df',number=1))

# 5 - Using pandas apply function
def using_apply(df):
    return df.apply(lambda x: x['A'] + x['B'], axis=1).sum()
print(timeit.timeit(stmt='using_apply(df)', setup='from __main__ import using_apply, df',number=1))


# 6 - Using pandas builtin add function
def using_pandas_builtin(df):
    return (df['A'] + df['B']).sum()
print(timeit.timeit(stmt='using_pandas_builtin(df)', setup='from __main__ import using_pandas_builtin, df',number=1))


# 7 - Using numpy builtin function
def using_numpy_builtin(df):
    return (df['A'].values + df['B'].values).sum()
print(timeit.timeit(stmt='using_numpy_builtin(df)', setup='from __main__ import using_numpy_builtin, df',number=1))





# References: https://medium.com/swlh/how-to-efficiently-loop-through-pandas-dataframe-660e4660125d