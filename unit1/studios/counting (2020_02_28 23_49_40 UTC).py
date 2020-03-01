def count_chars(text) :
	stats = {}
	
	for char in text:
		if char not in stats:
			stats[char] = 1
		else:
			stats[char] += 1
	
	for k,v in stats.items():
		print(k +":",v)

		
def main():
    text = str(input("Enter a string: "))
    count_chars(text)

if __name__ == '__main__':
    main()
