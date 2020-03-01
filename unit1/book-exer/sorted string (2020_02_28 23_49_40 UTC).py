def is_sorted(string):
    length=int(len(string))
    i=0
    for i in range(0,length-1):
        if string[i]>string[i+1]:
            i=i+1
            return False
    return True
                        