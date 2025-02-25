from pympler import asizeof
obj = [1, 2, (3, 4), 'text']
s = asizeof.asizeof(obj)
print(s)