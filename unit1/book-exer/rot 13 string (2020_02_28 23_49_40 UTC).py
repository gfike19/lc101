def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha_dict={}
    for char in alphabet:
        alpha_dict[char]=char.upper()
    num=0
    for char in letter:
        num=alpha_dict.get(char)
    return num

