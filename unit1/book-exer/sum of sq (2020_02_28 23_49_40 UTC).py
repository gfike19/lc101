def sum_of_squares(xs):
    sq_list=[]
    for i in xs:
        new_num=i*i
        sq_list.append(new_num)
    sum_sq=0
    for i in sq_list:
        sum_sq+=i
    return sum_sq

print(sum_of_squares([2,3,4]))