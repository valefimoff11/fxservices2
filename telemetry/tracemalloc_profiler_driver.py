import gc
import tracemalloc

import numpy as np
import pandas as pd

import tracemalloc_profiler

arr = []


def mem_leaker():
    '''Appends to a global array in order to simulate a memory leak.'''

    df1 = pd.DataFrame({
        'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
        'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
        'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
    })

    #arr.append(np.ones(10000, dtype=np.int64))

    arr.append(df1)

if __name__ == '__main__':
    tracemalloc.start(10)

    for _ in range(1):
        mem_leaker()
        gc.collect()
        tracemalloc_profiler.snapshot()

    tracemalloc_profiler.display_stats()
    tracemalloc_profiler.compare()
    tracemalloc_profiler.print_trace()