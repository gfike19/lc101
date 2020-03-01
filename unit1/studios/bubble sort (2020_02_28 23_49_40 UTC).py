def bubble_sort(lst):
    length = len(lst)
    is_sorted = False
    while is_sorted == False:
        nswaps = 0
        for i in range (0,(length - 1)):
            if lst[i] > lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                nswaps = nswaps+1
        if nswaps == 0:
            is_sorted = True
        else:
            is_sorted = False
    return lst   