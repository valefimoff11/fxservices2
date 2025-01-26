s = {"a":3, "b":4}

print("a" in s)
print(s.get("a"))

try:

    print(s["e"])

except KeyError as err:

    print(s["a"])

for v in s.values():
    print(v)

