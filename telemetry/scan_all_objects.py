import sys
import pandas as pd
import numpy as np

df2 = pd.DataFrame({
    'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
})

TEST_VAR = 1919

#add to this Class Reflection

global_vars = globals()
print(global_vars)

print("####################################################################")

local_vars = locals().copy()
print(local_vars)

print("####################################################################")

for var, obj in local_vars.items():
    if isinstance(obj, pd.DataFrame):
        gso = obj.memory_usage(True, True).sum()
        print(var + ": " + str(gso))

sys.exit()

all_vars = global_vars + local_vars
total = 0
mem = []
vars = []
for var, obj in all_vars:
    if isinstance(obj, pd.DataFrame):
        gso = obj.memory_usage().sum()
    elif isinstance(obj, np.ndarray):
        gso = obj.size
    else:
        gso = sys.getsizeof(obj)
    total += gso
    mem = mem + [gso]
    vars = vars + [var]
    print(var, gso)

df = pd.DataFrame({'obj': vars, 'size': mem}).sort_values('size', ascending=False)
print(df['size'].sum()/1000000)