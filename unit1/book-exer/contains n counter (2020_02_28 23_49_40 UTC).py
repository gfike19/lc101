def contains_n(numbers, number):
    counter=0
    for x in numbers:
        if number==x:
            counter=counter+1
    return counter

numbers=[2,4,6,2,8,10,2]

target=contains_n(numbers,2)

print(target)

# Be sure to test your function with various inputs
