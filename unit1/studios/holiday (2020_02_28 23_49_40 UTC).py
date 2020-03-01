currentDay=input("What day are you leaving on?")
currentDay=int(currentDay)
vacationTime=input("How many days will you be on vacation?")
vacationTime=int(vacationTime)
returnDate=(currentDay+vacationTime)%7
print("You will be back on day",returnDate)