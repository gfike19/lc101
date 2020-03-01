def check_group(ages):
    for age in ages:
        if age < 70:
            return False
        else:
            return True

def check_group(ages):
    for age in ages:
        if age < 70:
            return False #if greater than seventy cause no else statement has to check
    return True