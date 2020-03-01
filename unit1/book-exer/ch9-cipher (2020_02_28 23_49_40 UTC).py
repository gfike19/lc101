import secrets
import string
import random

def getCipher():
    baseNums = []

    for num in range(0,27):
        baseNums.append(num)
    
    newPos = []

    while len(newPos) < 26:
        newNum = secrets.randbelow(len(baseNums))
        newPos.append(baseNums.pop(newNum))
    
    allAlpha = string.ascii_uppercase

    cipher = {}

    for num in range(26):
        cipher[allAlpha[num % 26]] = allAlpha[newPos[num] % 26]
    
    return cipher

def encrypt(text, cipher):
    newText = ""

    for each in text:
        if each.isalpha == True:
            newText = newText + cipher[each.isupper()]
        else:
            newText = newText + each
    
    return newText

# def decrypt(text, cipher):
#     plain = ""

#     allVals = cipher.items()

#     for each in text:
        # find returns negative numbers, index returns value error
        

cipher = getCipher()
print("The cipher is:",cipher)

# text = input("Enter some text to encrypt: ")

# newMsg = encrypt(text, cipher)

# print("The encrypted message is:", newMsg)

letter = input("Enter a letter: ")

for k,v in cipher.items():
    if letter == v:
        print(k)
