import random
import string

def getCipher():
    
    #get all numbers from 0 -> 26
    baseNums = []
    
    for num in range(0,27):
        baseNums.append(num)
    
    #scramble the numbers, this will be the new positions for the letters
    newPos = []

    while len(newPos) < 26:
        rNum = random.randrange(0, sizeOfBaseNums)
        randomBaseNum = baseNums[rNum]
        numToRemove = randomBaseNum % sizeOfBaseNums
        newPos.append(baseNums.pop( % len(baseNums)))
    
    #gets all uppercase letters
    allAlpha = string.ascii_uppercase
    
    #gets each letter at the position indicated in newPos and adds it to the cipher string
    cipher = ""
    
    for num in newPos:
        cipher = cipher + allAlpha[num % 26]
    
    return cipher
    
def displayCipher(cipher):
    allAlpha = string.ascii_uppercase
  
    for num in range(26):
        print(allAlpha[num] + " --> " + cipher[num] + "\n")

cipher = getCipher()
displayCipher(cipher)