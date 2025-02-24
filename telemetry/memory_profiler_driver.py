import sys
import io
import numpy as np
import pandas as pd
from memory_profiler import profile

#Execute the code passing the option -m memory_profiler to the python interpreter to load the memory_profiler module and print to stdout
#the line-by-line analysis. If the file name was example.py, this would result in:
# python -m memory_profiler example.py

#for reporting and plotting
#mprof run executable
#mprof plot

@profile
def allocate_dummy_memory():

	# Allocate a list with a range of numbers
	a = [i for i in range(10000)]
	# Allocate another list with squares of numbers
	b = [i ** 2 for i in range(10000)]

	df1 = pd.DataFrame({
		'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
		'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
		'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
	})

	df1 = df1

	return a, b, df1

ds = allocate_dummy_memory()
ds1 = allocate_dummy_memory()


print("")

print( round( sys.getsizeof(ds[2])/1024/1024, 1) )

print("")

ds[2].info(memory_usage='deep')

print("")

ds[2].info()

#sys.exit()

###########################################################################

buffer = io.StringIO()

mem_logs = open('mem_profile.log','a')

@profile(stream=buffer)
def process_strs1(reps=10**6):
	str1 = 'python'*reps
	str2 = 'programmer'*reps
	str3 = str1 + str2
	print(sys.getsizeof(str3)/1024/1024)
	del str2
	return str3

process_strs1(reps=10**7)

df_info = buffer.getvalue()
print("------------------------------------------------------------------")
print(df_info)


############################################################################

from memory_profiler import memory_usage

#def process_strs(reps=10**6):
#	str1 = 'python'*reps
#	str2 = 'programmer'*reps
#	str3 = str1 + str2
#	del str2
#	return str3

#process_strs(reps=10**7)

#mem_used = memory_usage((process_strs,(),{'reps':10**7}),interval=0.01)
#print(mem_used)