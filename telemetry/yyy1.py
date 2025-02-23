import numpy as np
import pandas as pd

random_strings_array = np.random.choice(['a', 'b', 'c'], 10 ** 6)
df = pd.DataFrame({
    'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
})
df.info()
print("#####################################################")
df.info(memory_usage='deep')

print("111111111111111#######################################")
import io
buffer = io.StringIO()
df.info(memory_usage='deep', buf=buffer)
s = buffer.getvalue()
print(s)

print("#####################################################")
print(df.memory_usage(True, True))