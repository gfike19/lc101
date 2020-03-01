def print_triangular_numbers(n):
    i=int(1)
    while i<=n:
        triNum=int((i*(i+1))/2)
        print(i,'\t',triNum)
        i=i+1
        
print_triangular_numbers(5)