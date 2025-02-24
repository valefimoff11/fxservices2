import sys
from sys import getsizeof, stderr
import io
from itertools import chain
from collections import deque

import numpy as np
import pandas as pd

try:
    from reprlib import repr
except ImportError:
    pass


def get_pandas_mem_profile(df):
    """ Returns the total size, column size, mem footrpint related info and object reference count of Pandas dataframe """

    df_total_mem_size = sys.getsizeof(df)
    df_column_size = df.memory_usage(True, True)

    buffer = io.StringIO()
    df.info(memory_usage='deep', buf=buffer)
    df_info = buffer.getvalue()

    df_ref_count = sys.getrefcount(df) - 1

    return df_total_mem_size, df_column_size, df_info, df_ref_count


def get_container_total_size(o, handlers={}, verbose=False):
    """ Returns the approximate memory footprint of an container object and all of its items.

    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, deque, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:

        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}

    """
    dict_handler = lambda d: chain.from_iterable(d.items())
    all_handlers = {tuple: iter,
                    list: iter,
                    deque: iter,
                    dict: dict_handler,
                    set: iter,
                    frozenset: iter,
                   }
    all_handlers.update(handlers)     # user handlers take precedence
    seen = set()                      # track which object id's have already been seen
    default_size = getsizeof(0)       # estimate sizeof object without __sizeof__

    def sizeof(o):
        if id(o) in seen:       # do not double count the same object
            return 0
        seen.add(id(o))
        s = getsizeof(o, default_size)

        if verbose:
            print(s, type(o), repr(o), file=stderr)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)


if __name__ == '__main__':

    #d = dict(a=1, b=2, c=3, d=[4,5,6,7], e='a string of chars')

    df1 = pd.DataFrame({
        'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
        'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
        'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
    })

    df2 = pd.DataFrame({
        'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
        'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
        'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
    })

    input_ds = {"a": df1, "b": df2}

    print(get_container_total_size(input_ds, verbose=True))

    df_mem_profile = get_pandas_mem_profile(df1)
    print(df_mem_profile)

    print("")

    print(df_mem_profile[2])

    print("")

    #make use of the mem sizes of each column in the pandas dataframe
    for index, value in df_mem_profile[1].items():
        print(f"Index : {index}, Value : {value}")
