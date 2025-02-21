import gc
import tracemalloc

import numpy as np

import tracemalloc_profiler

arr = []


def mem_leaker():
    '''Appends to a global array in order to simulate a memory leak.'''
    arr.append(np.ones(10000, dtype=np.int64))


if __name__ == '__main__':
    tracemalloc.start(10)

    for _ in range(5):
        mem_leaker()
        gc.collect()
        tracemalloc_profiler.snapshot()

    tracemalloc_profiler.display_stats()
    tracemalloc_profiler.compare()
    tracemalloc_profiler.print_trace()