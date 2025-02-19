from memory_profiler import profile

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

############################################################################

from memory_profiler import memory_usage

def process_strs(reps=10**6):
	str1 = 'python'*reps
	str2 = 'programmer'*reps
	str3 = str1 + str2
	del str2
	return str3

process_strs(reps=10**7)

#mem_used = memory_usage((process_strs,(),{'reps':10**7}),interval=0.01)
#print(mem_used)