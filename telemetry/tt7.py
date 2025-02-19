import tracemalloc

import numpy as np
import pandas as pd

tracemalloc.start(10)                      # Set stack depth
time1 = tracemalloc.take_snapshot()        # Before snapshot

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

time2 = tracemalloc.take_snapshot()        # After snapshot

stats = time2.compare_to(time1, 'lineno')  # Compare snapshots
for stat in stats[:3]:
    print(stat)
    print(stat.traceback.format())
