alphabet = 'abcdefghijklmnopqrstuvwxyz' #global variables are declared outside of the functions so all functions can access them
alpha_cap=str(alphabet.upper()) #uppercased version of alphabet


def alphabet_position(letter):
    pos = 0 #pos = position
    
    for char in letter: #loops thru the given given letter, char is a temporary variable
        alpha_pos = alphabet.find(char)#finds the position of char in the alphabet strings, emphasis on find since index returns a runtime error if an item is not found, we don't want the function to give us an error
        caps_pos = alpha_cap.find(char)
        
    if alpha_pos >= 0:#if the position found in the alphabet string is greater than 0 then that's the position of the letter being passed through
        pos += alpha_pos# += is the same as pos = pos + alpha_pos
        
    if caps_pos >= pos:#the point of this was to make sure if a capiral letter was used that its position was returned
        #is incorrect need to use an if statement and alphabet.find(char) and whether that comes back true to determine which version of the alphabet to check
        pos += caps_pos
        
    return pos

def rotate_character(char, rot):
    
    po s= alphabet_position(char)#use the previous function to return the position of the char being passed thru rotate_character
    pos_caps =a lphabet_position(char)
    
    new_cap_pos = pos_caps+rot#new position is position of the character plus the rotation given by the user when they call this function
    new_pos = pos + rot
    
    if new_cap_pos > 25 or new_cap_pos < 0:#however if the new position falls outside of the length of the alphabet string or is less than zero then the position should just be the rotation
        new_cap_pos = rot
 
    if new_pos > 25 or new_pos < 0:
        new_pos = rot
    
    new_char = alphabet[new_pos]#using the new position find the new character
    new_char_caps = alpha_cap[new_cap_pos]

    return new_char,new_char_caps

#any previous print statements were used for test purposes and are not needed
