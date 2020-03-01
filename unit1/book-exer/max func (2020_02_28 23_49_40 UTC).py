import random

def max(lst):
    max = 0
    for e in lst:
        if e > max:
            max = e
    return max

lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(max(lst))