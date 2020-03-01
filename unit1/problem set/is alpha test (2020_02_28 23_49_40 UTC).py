def test():
    text=input("What is the phrase to test?"+"\n")#Prints a prompt line to inform the user what to do, "\n" creates a new line so the user's text will go underneath the prompt
    string = str(text)#ensures that the text being passed thru the function is a string
    alpha_chars = ''#empty string where the alphabetic characters will go
    non_alpha_chars = ''#empty string where the non alphabetic characters will go
    for char in string: #for every item in the string do the following
        if char.isalpha() == True: #if it is an alphabetic character, do the following
            alpha_chars+=char#adds the character to the string of alphabetic ones
        else: #if the character is not an alphabetic one, do the following
            non_alpha_chars += char#adds the character to the string of non alphabetic ones
    return "The alphabetic characters are "+alpha_chars+" and the non alphabetic characters are "+non_alpha_chars #don't need to type this as a string since all items being added are string type


