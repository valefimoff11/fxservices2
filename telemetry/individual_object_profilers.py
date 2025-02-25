import sys
from sys import getsizeof, stderr
import io
from itertools import chain
from collections import deque
import numpy as np
import pandas as pd
from reprlib import repr


def optimize_data_size_unit(nbytes):

    data_size_suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

    i = 0
    while nbytes >= 1024 and i < len(data_size_suffixes)-1:
        nbytes /= 1024
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, data_size_suffixes[i])

#df.memory_usage(index=True, deep=True).apply(optimize_data_size_unit)
# Index  128 B
# a      571.72 MB
# b      687.78 MB
# c      521.6 MB
# dtype: object
#optimize_data_size_unit(df.memory_usage(index=True, deep=True).sum())

def get_pandas_mem_profile(df):
    """ Returns the total size, column size, mem footrpint related info and object reference count of Pandas dataframe """

    df_total_mem_size = sys.getsizeof(df)
    df_column_size = df.memory_usage(True, True)
    df_total_mem_size2 = df_column_size.sum()

    buffer = io.StringIO()
    df.info(memory_usage='deep', buf=buffer)
    df_info = buffer.getvalue()

    df_ref_count = sys.getrefcount(df) - 1

    return df_total_mem_size, df_total_mem_size2, df_column_size, df_info, df_ref_count


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

    d1 = dict(a=1, b=2, c=3, d=[4,5,6,7], e='a string of chars')
    print(get_container_total_size(d1, verbose=False))

    print("")

    d2 = dict(a=1, b=2, c=3, d=[4,5,6,7, 88, 222, 333, 37373, 777, 3333, 333, 333, 33], e='a string of chars')
    print(get_container_total_size(d2, verbose=False))

    print("")

    from pympler import asizeof
    s = asizeof.asizeof(d1)
    print(s)
    s = asizeof.asizeof(d2)
    print(s)

    df1 = pd.DataFrame({
        'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
        'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
        'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
    })

    s = asizeof.asizeof(df1)
    print(s/1024/1024)

    print()

    df_mem_profile = get_pandas_mem_profile(df1)
    print(df_mem_profile)

    print()

    print(asizeof.asized(df1, detail=1).format())
    print()
    print(asizeof.flatsize(df1, detail=1))


    sys.exit()

    # Allocate a list with a range of numbers
    a = [i for i in range(10000)]
    print(get_container_total_size(a, verbose=False))

    print("")

    # Allocate another list with squares of numbers
    b = [i ** 2 for i in range(10000)]
    print(get_container_total_size(b, verbose=False))

    print("")

    print(sys.getsizeof(b))

    sys.exit()

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

    print(df_mem_profile[3])

    print("")

    #make use of the mem sizes of each column in the pandas dataframe
    for index, value in df_mem_profile[2].items():
        print(f"Index : {index}, Value : {value}")

    print("")

    print(df_mem_profile[0])
    print(df_mem_profile[1])

