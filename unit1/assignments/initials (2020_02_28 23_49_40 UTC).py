def initials(string):
    i = string.find(" ")
    first = str(string[0])
    afterSpace = i + 1
    second = str(string[afterSpace])
    init = first + second
    return init

print(initials("Jane Doe"))