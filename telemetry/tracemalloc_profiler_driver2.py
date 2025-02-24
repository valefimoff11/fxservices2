import tracemalloc

tracemalloc.start()

def allocate_memory():
    a = [i for i in range(10000)]
    b = [i ** 2 for i in range(10000)]
    return a, b

r = allocate_memory()

snapshot = tracemalloc.take_snapshot( )
top_stats = snapshot.statistics('lineno')

for stat in top_stats[:10]:
    print(stat)