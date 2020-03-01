import random
alist=[]
for i in range(0,11):
    alist.append(random.randrange(0,101))
print(alist)
alist.insert(2,19)
print(alist)