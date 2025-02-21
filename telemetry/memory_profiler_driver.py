from memory_profiler import profile

#Execute the code passing the option -m memory_profiler to the python interpreter to load the memory_profiler module and print to stdout
#the line-by-line analysis. If the file name was example.py, this would result in:
# python -m memory_profiler example.py

#for reporting and plotting
#mprof run executable
#mprof plot

@profile
def process_strs(reps=10**6):
	str1 = 'python'*reps
	str2 = 'programmer'*reps
	str3 = str1 + str2
	del str2
	return str3

process_strs(reps=10**7)

###########################################################################

mem_logs = open('mem_profile.log','a')

@profile(stream=mem_logs)
def process_strs(reps=10**6):
	str1 = 'python'*reps
	str2 = 'programmer'*reps
	str3 = str1 + str2
	del str2
	return str3

process_strs(reps=10**7)
process_strs(reps=10**7)


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