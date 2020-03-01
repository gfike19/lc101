# Write a program that calculates the number of times each character 
# occurs in a string and prints these stats to the console. You could get 
# the string as input from the user, but for the sake of simplicity, you may 
# also hard-code the string into your program as the value of a variable. Here’s a 
# test string, for your convenience:

def counting(text):
    letters = {}

    for char in text:
        number = text.count(char)
        letters[char] = number
    return letters


def main():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."
    count_dict = counting(text)
    print(count_dict.items())
main()
