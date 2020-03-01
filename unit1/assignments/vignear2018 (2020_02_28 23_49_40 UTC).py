import string

alpha = string.ascii_lowercase

def alphaPos(char):
    return alpha.find(char)

def rotateChar(char, pos):
    currPos = alphaPos(char)
    newPOs = (currPos + pos)
    newPOs = newPOs % 26
    return alpha[newPOs]

def vingear(text, keyword):
    keyLen = len(keyword)
    idx = 0
    newText = ""

    for char in text:
        idx %= keyLen
        rot = alphaPos(keyword[idx])

        if char.isalpha():           
            newChar = rotateChar(char, rot)
            newText = newText + newChar
            idx += 1  

        else:
            newText = newText + char

    return newText

def main():
    text = input("Enter the plain text: ")
    keyword = input("Enter the key: ")
    print("New message is:", vingear(text, keyword))