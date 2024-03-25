# Excersice 2: Good Morning Sir
# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp1 = int(time.strftime('%H'))
print(timestamp1)
if(timestamp1<0):
    print("Number is not in time zone")
elif(timestamp1>0):
    if(timestamp1<12):
        print("Good Morning sir")
    elif(timestamp1==12):
        print("Good Morning sir")
    elif(timestamp1>12):
        print("Good Afternoon sir")
    elif(timestamp1<=18):
        print("Good Afternoon sir")
    elif(timestamp1>18):
        print("Good Evening sir ")
    else:
        print("Good Night")
else:
    print("technical error")


     
