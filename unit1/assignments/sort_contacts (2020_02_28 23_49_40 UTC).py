def sort_contacts(tuplex):
    names = []
    for k,v in tuplex.items():
        names.append(k)

    names = sorted(names)
    aList = []
    

    for name in names:
        contact = tuplex[name]
        val1 = contact[0]
        val2 = contact[1]
        tup = (name, val1, val2)
        aList.append(tup)
    
    return aList


print(sort_contacts({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
        "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
        "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}), [('Freud, Anna', '1-541-754-3010',
        'anna@psychoanalysis.com'), ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'),
        ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')])
