def char_count(string):
    string=str(string)
    string_list=string.split()
    count=0
    for i in string_list:
        if len(i)==5:
            count+=1
    return count

print(char_count("fives taste touch sound"))