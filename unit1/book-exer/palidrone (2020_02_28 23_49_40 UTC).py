def isPalidrone(string): #instead of ignore case, convert to upper or lower
    length-len(string)
    for pos in range (0,length):
        if string[-(pos+1)]!=string[pos]: #b/c checking for == will get it stuck
            return False
    return True
        
print(isPalidrone("hannah"))
print(isPalidrone("racecar"))
print(isPalidrone("palidrone"))