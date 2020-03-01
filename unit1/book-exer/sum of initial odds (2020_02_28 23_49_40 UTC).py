def sum_of_initial_odds(nums):
    sums=0
    for i in nums:
        if i%2==0:
            return sums
        else:
            sums+=i
    return sums