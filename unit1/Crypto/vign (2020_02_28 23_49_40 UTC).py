from helpers import *

def cipher(message, key):
    i = 0
    key_len = len(key)#variable to hold the length of the key
    new_mess = ""
    rot = []

    for char in key:
        rot.append(alphabet_position(char))

    for i in range(key_len):
        for char in message:
            if char.isalpha():
                new_char = rotate_character(char,rot[i])
                i = i + 1
                new_mess = new_mess + new_char
                i = i%key_len
            else:
                new_mess += char
            
    return new_mess
            
            
              

# print(cipher("testing","boom"))
print(cipher("palindrone", "midnight"))
