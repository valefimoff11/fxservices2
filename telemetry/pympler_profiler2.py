import numpy as np
import pandas as pd
from pympler import summary, muppy
o1 = muppy.get_objects()
a = {}
b = {}
c = {}
d = {'a': [0, 0, 1, 2], 't': [3, 3, 3, 1]}

df1 = pd.DataFrame({
    'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
})

o2 = muppy.get_objects()
summary.print_(summary.get_diff(summary.summarize(o1), summary.summarize(o2)))