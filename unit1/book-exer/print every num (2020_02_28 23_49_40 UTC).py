def print_every(i, nums):
    counter = 0
    for i in nums:
        if counter % i == 0:
            print(i)
        counter += 1



def print_every(i, nums):
    counter = len(nums)
    for x in range (0,counter,i):
        print(nums[x])
