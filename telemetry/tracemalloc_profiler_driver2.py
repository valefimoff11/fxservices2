import sys
import tracemalloc

import numpy as np
import pandas as pd

tracemalloc.start(20)

def allocate_memory():
    #a = [i for i in range(10000)]
    #b = [i ** 2 for i in range(10000)]

    df1 = pd.DataFrame({
        'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
        'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
        'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
    })

    #print(sys.getsizeof(df1)/1024/1024)
    #print(df1.memory_usage().sum()/1024/1024)

    return df1

    #return a, b

r = allocate_memory()

snapshot = tracemalloc.take_snapshot( )
top_stats = snapshot.statistics('lineno')

for stat in top_stats[:10]:
    print(stat)

snapshot = snapshot.filter_traces((
    tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
    tracemalloc.Filter(False, "<frozen importlib._bootstrap_external>"),
    tracemalloc.Filter(False, "<unknown>"),
))
largest = snapshot.statistics("traceback")[0]

print(f"\n*** Trace for largest memory block - ({largest.count} blocks, {largest.size / 1024} Kb) ***")
for l in largest.traceback.format():
    print(l)