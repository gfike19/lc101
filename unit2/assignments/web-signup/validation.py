def no_spaces(string):
    for char in string:
        if char == " ":
            return False
    return True      

def is_empty(string):
    if string == " " or string == "":
        return True
    return False

def valid_len(string):
    if len(string) < 3 or len(string) > 20:
        return False
    return True

def valid_uname(uname):
    if not is_empty(uname) and valid_len(uname) and no_spaces(uname):
        return True
    return False

def valid_pwd(pwd):
    if not is_empty(pwd) and valid_len(pwd) and no_spaces(pwd):
        return True
    return False

def valid_email(email):
    p_count = 0
    at_count = 0
    for char in email:
        if char == ".":
            p_count += 1
        elif char == "@":
            at_count += 1

    if not valid_len(email) or p_count > 1 or at_count > 1  or not no_spaces(email):
        return False
    return True
