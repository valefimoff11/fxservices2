import sys

import numpy as np
import pandas as pd
import logging

random_strings_array = np.random.choice(['a', 'b', 'c'], 10 ** 6)
df = pd.DataFrame({
    'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
})

df2 = pd.DataFrame({
    'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
})

logging.basicConfig(level=logging.DEBUG)
logging.info("logging starts")


df.info()

print("###############################################")

print( round( sys.getsizeof(df)/1024/1024, 1) )

p = {"a" : df, "b" : df2}
print( round( sys.getsizeof(p)/1024/1024, 1) )

print("deep ###############################################")

df.info(memory_usage='deep')
df.info()


print("deep substring #######################################")

import io
buffer = io.StringIO()
df.info(memory_usage='deep', buf=buffer)
s = buffer.getvalue()
logging.info(s)

print("#####################################################")

print(df.memory_usage(True, True))

dmu = df.memory_usage(True, True)
for index, value in dmu.items():
    print(f"Index : {index}, Value : {value}")