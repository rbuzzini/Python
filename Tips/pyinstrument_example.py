import pandas as pd
from pyinstrument import Profiler
import numpy as np

df = pd.DataFrame({'num': np.random.randint(0, 100, 10000)})
df.head()

def is_even(num: int) -> int:
    return num % 2 == 0

profiler = Profiler()
profiler.start()

df = df.assign(is_even=lambda df_: is_even(df_.num))

profiler.stop()
#print(df.head())
profiler.print()
print(df.head())

