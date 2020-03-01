def sum_evens(alist):
    even_nums=0
    for num in alist:
        if num%2==0:
            even_nums=even_nums+num
    return even_nums