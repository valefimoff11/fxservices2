import numpy as np
import pandas as pd

ar = np.array([[1,2,3],[4,5,6]])

print(ar)

for x in ar:
    for y in x:
        print(y)

print(ar[0])

for x in np.nditer(ar):
    print(x)