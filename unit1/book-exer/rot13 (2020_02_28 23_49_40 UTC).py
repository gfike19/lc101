def rot13(mess):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in mess:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            rotated_index = alphabet.index(char) + 13
            if rotated_index < 26:
                encrypted = encrypted + alphabet[rotated_index]
            else:
                encrypted = e