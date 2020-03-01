def alphabet_position(character) :
    clean_char=character.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    num=0
    for char in clean_char:
        num=alphabet.index(char)
    return num

print(alphabet_position("l"))
print(alphabet_position("A"))
print(alphabet_position("u"))
print(alphabet_position("N"))
print(alphabet_position("c"))
print(alphabet_position("H"))