def cipher(message, key):
    for i in key:
        for char in message:
            print("The message character is: ",char,"\t ","The key value is: ", i)
   
KEEP CODE ABOVE

for i in range(rot_len-1):#runs a loop through the length of the rotation sequence up to but not including the last value
        for char in message:#runs a loop through the entire message
            print("The message character is: ",char,"\t ","The key value is: ", rot[i])

    key_len = len(key)

    mess_len = len(message)

    new_mess = ""

    for i in range (0,key_len-1):
        for j in range (0,mess_len-1):
            if message[j].isalpha() == True:
                print("Message at: ",j," is ",message[j],"\t","Key at: ",i," is ",key[i])
                new_mess += rotate_character(message[j],alphabet_position(key[i]))
                print("New message is now: ",new_mess)
            else:
                new_mess += message[j]

    i=0

    for i in key:
        for i in range(len(message)-1):
            print("The message character is: ",message[i],"\t ","The key value is: ",key[i])
    i += 1

    i = 0
    for i in range(len(message)):
        print(message[i])
        for i in range(len(key)):
            print(key[i])

#add to dictionary then try to vale values in dictionary through func
from helpers import *
str_dict={}

string = str(input("Enter a message: "))

key = str(input("Enter a key: "))

rot_seq = []

for char in key:
    rot_seq.append(alphabet_position(char))

print(rot_seq)

for char in string:
        for i in range(0,(len(string)-1)):
            str_dict[i] = (char,alphabet_position(char) + rot_seq[i]))
        if i > len(rot_seq) or i < 0:
            i -= len(rot_seq)

print(str_dict)

    i += 0

for char in message:
        for char0 in key:
            print(char,"\t",char0)

    split_mess = message.split()
    rot_seq = []

    for char in key:
        rot_seq.append(alphabet_position(char))

    new_mess = ""

    for word in split_mess:
        print(word)
        for char in word:
            print(char)
            for i in range(len(rot_seq)-1):
                print(i)
                new_mess += str(rotate_character(char,rot_seq[i]))


message = str(input("Enter a message: "))
key = str(input("Enter a key: "))
new_mess = ""

for char2 in key:
    for char in message:
        new_mess += rotate_character(char,alphabet_position(char2))

print(new_mess)


message = str(input("Enter a message: "))
key = str(input("Enter a key: "))

org_pos = []
rot_seq = []
new_seq = []

for char in message:
    org_pos.append(alphabet_position(char))

for char in key:
    rot_seq.append(alphabet_position(char))

for i in org_pos:
    new_seq.append(org_pos[i] + rot_seq[i])
    

new_char = rotate_character(char, rot[i])
            i += 1
            new_mess += new_char
            i = rot_len % i
        else:
            new_mess += char