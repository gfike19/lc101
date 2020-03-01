def contains_n(numbers, number):
    for x in numbers:
        if number==x:
            return True
    return False

numbers=[2,4,6,8,10]

print(contains_n(numbers,3))