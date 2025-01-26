class Cnt:

    def __init__(self, ai):
        self.a = ai

    def add(self, aa):
        return aa + self.a


a = 7

p = {"a":2, "b":3}

def f(x):
    x = x - 1
    a = 9
    print(x)

def ff(p):
    p["a"] = 100

def ac(c):
    c.a = 9999

x = 5

print(x)
f(x)
print(x)

print(a)

print(p)
ff(p)
print(p)

c = Cnt(10)
print(c.a)
ac(c)
print(c.a)

