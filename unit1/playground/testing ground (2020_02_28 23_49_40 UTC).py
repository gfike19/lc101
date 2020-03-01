from helpers import *

def cipher(message, key):
     key_len = len(key)

     for i in range(key_len):
         print(key[i])

print(cipher("testing","boom"))
