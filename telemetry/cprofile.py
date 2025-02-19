import cProfile

import pstats


def my_function():

    # Your code here
    pass

if __name__ == "__main__":

    profiler = cProfile.Profile()

    profiler.enable()

    my_function()

    profiler.disable()

    stats = pstats.Stats(profiler)

    stats.sort_stats(pstats.SortKey.TIME)

    stats.print_stats()