def analyze_text(text):
    string=str(text)
    numofchars=0
    for char in string:
        if char.isalpha()==True:
            numofchars=numofchars+1
    numofe=int(string.count("E")+string.count("e"))
    percente=float((numofe/numofchars)*100)
    statement=str("The text contains "+str(numofchars)+" alphabetic characters, of which "+str(numofe)+" ("+str(percente)+"%) are 'e'.")
    return statement