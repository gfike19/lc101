import random

def make_lst():
    count = int(input("How many numbers do you need? "))
    lowest = int(input("What's the lowest number? "))
    upper = int(input("What's the highest number? ")) + 1     
    lst=[]
    for i in range (0,count):
        lst.append(random.randrange(lowest,upper))
    return lst

lst = make_lst()
print(lst)