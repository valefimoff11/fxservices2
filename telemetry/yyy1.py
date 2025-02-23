import numpy as np
import pandas as pd

random_strings_array = np.random.choice(['a', 'b', 'c'], 10 ** 6)
df = pd.DataFrame({
    'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
})

df.info()

print("deep ###############################################")

df.info(memory_usage='deep')

print("deep substring #######################################")

import io
buffer = io.StringIO()
df.info(memory_usage='deep', buf=buffer)
s = buffer.getvalue()
print(s[1])

print("#####################################################")

print(df.memory_usage(True, True))

dmu = df.memory_usage(True, True)
for index, value in dmu.items():
    print(f"Index : {index}, Value : {value}")