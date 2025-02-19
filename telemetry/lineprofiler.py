from line_profiler import LineProfiler

def example_function():

# Your code here

    pass

profiler = LineProfiler()

profiler.add_function(example_function)

profiler.enable_by_count()

example_function()

profiler.print_stats()