alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha_cap = str(alphabet.upper())


def alphabet_position(letter):
    
    pos = 0
    
    for char in letter:
        if char in alphabet:
            pos = alphabet.find(char)
        if char in alpha_cap:
            pos = alpha_cap.find(char) 
    return pos


def rotate_character(char, rot):
    
    if char in alphabet:
        pos = alphabet_position(char)
        new_pos = pos + rot
        new_pos %= 26
        new_char = alphabet[new_pos]
        return new_char
        
    if char in alpha_cap:
        pos_caps = alphabet_position(char)
        new_cap_pos = pos_caps + rot
        new_cap_pos %= 26
        new_char_caps = alpha_cap[new_cap_pos]
        return new_char_caps


def encrypt(text, key):
    i = 0
    rot_len = len(key)
    new_mess = ""

    for char in text:
        i %= i % rot_len #ensures i falls within range of the message
        rot = alphabet_position(key[i])
        if char.isalpha():
            new_char = rotate_character(char,(rot))
            new_mess += new_char
            i += 1
        else:
            new_mess += char
        

    return new_mess

print(encrypt("The crow flies at midnight","boom"))