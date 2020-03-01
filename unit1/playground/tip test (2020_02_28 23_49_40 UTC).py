choice="y"
while (choice==y): 
    sub=input("What is the cost of the meal before tip?")
    sub=float(sub)
    tipPercent=input("What percentage would you like to tip?")
    tipPercent=float(tipPercent)/100
    total=float((sub*tipPercent)+sub)
    print("The total cost of the meal is",total)
    choice=input("Repeat?")
