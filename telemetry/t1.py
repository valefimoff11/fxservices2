import sys
import numpy as np
import pandas as pd

add = "memory"
ref_count = sys.getrefcount(add)
print(ref_count)

class Gfg_class:
    a = 20

# creating instance of class
obj = Gfg_class()
obj2 = obj
ref_count = sys.getrefcount(obj)
print(ref_count)

# delete object using del
del obj

ref_count = sys.getrefcount(obj2)
print(ref_count)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

ref_count = sys.getrefcount(df2)
print(ref_count)
#total RAM
print( df2.info() )
#RAM by column
print(df2.memory_usage())

#print( df2["A"] )
#print( df2["A"].info() )

ref_count = sys.getrefcount(df2)
print(ref_count)

df3 = df2

ref_count = sys.getrefcount(df2)

del df3

ref_count = sys.getrefcount(df2)
print(ref_count)


df4 = df2[["A", "B"]]
print(df4)
ref_count = sys.getrefcount(df4)
print(ref_count)
#total RAM
print( df4.info() )
#RAM by column
print(df4.memory_usage())

print("metrics for df2")

ref_count = sys.getrefcount(df2)
print(ref_count)
#total RAM
print( df2.info() )
#RAM by column
print(df2.memory_usage())


sys.exit()

#pandas chunking
# Reading the data in chunks
data = pd.read_csv('data.csv', chunksize=1000)
# Concatenating the chunks together
df = pd.concat(data)