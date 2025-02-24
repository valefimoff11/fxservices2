import tracemalloc

import numpy as np
import pandas as pd

tracemalloc.start(10)

def allocate_memory():
    a = [i for i in range(10000)]
    b = [i ** 2 for i in range(10000)]

    df1 = pd.DataFrame({
        'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
        'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
        'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
    })

    return a, b, df1

r = allocate_memory()

snapshot = tracemalloc.take_snapshot( )
top_stats = snapshot.statistics('lineno')

for stat in top_stats[:10]:
    print(stat)