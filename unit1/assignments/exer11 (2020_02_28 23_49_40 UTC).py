def stu_roster():
    students = {}

    # Use a space to allow for the while check below
    new_student = " "

    # Get student names
    while (new_student != ""):
        new_student = input("Student's name (or press ENTER to finish)")
        if new_student != "":
            students[new_student] = 0

    # Get student grades
    for student in students.keys():
        new_grade = float(input("Grade for " + student + ": "))
        students[student] = new_grade


    for k,v in students.items():
        print(k,v)

# def pirate():
    # pirate_talk = {"sir":"matey", "hotel":"fleabag inn", "student":"swabbie", "boy":"matey", "madam":"proud beauty", "professor":"foul blaggar", "restaurant":"galley", "your":"yer", "excuse":"arr", "students":"swabbles", "are":"be", "lawyer":"foul blaggart", "restroom":"th' head", "my":"me", "hello":"avast", "is":"be", "man":"matey"}
    # text = input("Enter a sentence: ")
    # for word in text:
    #     text = text.split()
    #     print(text)
    # new_text = ""
    # for word in text:
    #    if pirate_talk.get(word) == True:
    #        new_text += pirate_talk.get(word)
    # else:
    #     new_text += word
    # print("pirate ver is:",new_text)
def translate(text):
# your code here!
    pirate_talk = {"sir":"matey", "hotel":"fleabag inn", "student":"swabbie", "boy":"matey", "madam":"proud beauty", "professor":"foul blaggar", "restaurant":"galley", "your":"yer", "excuse":"arr", "students":"swabbles", "are":"be", "lawyer":"foul blaggart", "restroom":"th' head", "my":"me", "hello":"avast", "is":"be", "man":"matey"}
    new_text = ""
    text_lst = list(text.split())
    for word in text_lst:
        if pirate_talk.get(word):
            new_text += pirate_talk.get(word) + " "
        else:
            new_text += word + " "
    return new_text

def main():
    # repeat = "y"
    # while repeat == "y":
    #     choice = int(input("Which func should I run?\n1) stu_roster\n2) pirate\n"))
    #     if choice == 1:
    #         stu_roster()
    #     elif choice == 2:
    #         pirate()
    #     print("\n")
    #     repeat = input("repeat? (y/n)")
    print(translate("hello my man, please excuse your professor to the restroom!"))


if __name__ == '__main__':
    main()