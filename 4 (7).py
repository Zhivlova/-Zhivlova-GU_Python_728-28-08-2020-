from math import factorial

def generator():
    for el in factorial(n):
        yield el
g = generator()
print(g)