def bubble_sort(alist):
    is_sorted = False
    while is_sorted == False:
        num_swaps = 0
        for idx in range(0,(len(alist)- 1)):
            # a = alist[idx]
            # b = alist[idx + 1]
            if alist[idx] > alist[idx + 1]:
                temp = alist[idx + 1]
                alist[idx + 1] = alist[idx]  
                alist[idx] = temp
                num_swaps = num_swaps + 1
        if num_swaps == 0:
            is_sorted = True
        else:
            is_sorted = False
    return alist