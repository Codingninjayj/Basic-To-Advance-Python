import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp1 = int(time.strftime('%H'))
print(timestamp1)
if(timestamp1<0):
    print("Number is not in time zone")
elif(timestamp1>0):
    if(timestamp1<12):
        print("Good Morning")
    elif(timestamp1==12):
        print("Good Morning")
    elif(timestamp1>12):
        print("Good Evening")
    elif(timestamp1<=18):
        print("Good Afternoon")
    elif(timestamp1>18):
        print("Good Evening")
    else:
        print("Good Night")
else:
    print("technical error")


     
