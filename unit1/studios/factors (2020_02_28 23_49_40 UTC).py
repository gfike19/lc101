def factors(n):
	dikt = {}
	while n != 0:
		lst = []
		
		for i in range(1, n + 1):
			if n % i == 0:
				lst.append(i)
		dikt [n] = lst
		n -= 1
	return dikt


f_dict = factors(15)

for k,v in f_dict.items():
		print(k,v)