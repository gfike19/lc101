
currentTime=input("What is the current time?")
currentTime=int(currentTime)
alarmTime=input("Number of hrs to wait for alarm?")
alarmTime=int(alarmTime)
wakeTime=currentTime+alarmTime%24-12
if wakeTime<=11:
    print("The alarm will go off at",wakeTime,"am")
    
elif wakeTime>11:
    print("The alarm will go off at",wakeTime,"pm")
    
