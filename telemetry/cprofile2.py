#You can combine timeit and cProfile to get detailed insights. Use timeit for precise timing
#and cProfile for comprehensive profiling

import cProfile

import timeit


def example_function():

# Your code here

    pass

if __name__ == "__main__":

# Using timeit

    setup_code = "from __main__ import example_function"

    stmt = "example_function()"

    print(timeit.timeit(stmt, setup=setup_code, number=1000))

    # Using cProfile

    profiler = cProfile.Profile()

    profiler.enable()

    example_function()

    profiler.disable()

    profiler.print_stats(sort='time')