import gc
import tracemalloc

import numpy as np

import profiler

arr = []


def mem_leaker():
    '''Appends to a global array in order to simulate a memory leak.'''
    arr.append(np.ones(10000, dtype=np.int64))


if __name__ == '__main__':
    tracemalloc.start(10)

    for _ in range(5):
        mem_leaker()
        gc.collect()
        profiler.snapshot()

    profiler.display_stats()
    profiler.compare()
    profiler.print_trace()