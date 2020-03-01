def is_prime(num):
    i=1
    factors=0
    while i<num:
        if num%i==0:
            factors=factors+1
        i=i+1
    if factors==1:
        return True
    if factors>=1:
        return False