def get_initials(fullname):
    name = fullname.split()
    init = ""
    for i in name:
        init +=i[0]
    return init.upper()

print(get_initials("HULK"))
