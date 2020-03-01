from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    i = 0
    rot_len = len(key)
    new_mess = ""

    for char in text:   
        i %= rot_len #ensures i falls within range of the message
        rot = alphabet_position(key[i])
        if char.isalpha():
            new_char = rotate_character(char,rot)
            new_mess += new_char
            # i is incremented to go along length of org text
            i += 1
        else:
            new_mess += char
        

    return new_mess

def main():
    text = input("Enter a message: ")
    key = input("Enter a keyword: ")
    print(encrypt(text, key))

if __name__ == "__main__":
    main()