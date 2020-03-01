import string
#TODO get list of all names and then sort that, then call values from dictionary

dictionary = {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
"Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
"Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}


name_lst = []

for k,v in dictionary.items():
    name_lst.append(k)

letters = string.ascii_letters
sorted_names = sorted(name_lst)

new_dict = {}

for name in sorted_names:
    val = dictionary[name]
    new_dict[name] = val

for k, v in new_dict.items():
    print(k)
    for each in v:
        print(each)
