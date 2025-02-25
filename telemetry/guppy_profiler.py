import sys

import numpy as np
import pandas as pd
from guppy import hpy

h=hpy()

h.setrelheap()
#h.setref()

df1 = pd.DataFrame({
    'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
})

before = h.heap()
print(before)

df2 = pd.DataFrame({
    'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
})

dd = {"df1": df1, "df2": df2}


after = h.heap()
print(after.all)
print(len(after))

sys.exit()

print()
print(h.iso(df2).sp)
print()
print(h.iso(df1, df2))
print()
print(h.iso(dd))
print()
print(after[0])
print(after.bytype)
print(after.byrcs)
print(after.byid)

delta = after - before

print("printing the DELTA ######################")

print(delta)

print()


print( h.heap().get_rp(40) )

#import resource
#print('Memory usage: %s (kb)' % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
