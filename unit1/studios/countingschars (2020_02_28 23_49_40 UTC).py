text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."

def countingChars(text):

    dit = {}

    for each in text:
        dit[each] = 0
    
    for each in text:
        val = dit[each] + 1
        dit[each] = val
    
    return dit
            
print(countingChars(text))
      