# Python while Loop
# As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.


#Example:1
i=0
while(i<5):
    print(i)
    i=i+1


# #Example:2
i=int(input("Enter your number:"))
while(i<=38):
    i=int(input("Enter your number:"))
    print(i)
print("Done with the loop")


# Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever.


#Example 3:
count=5
while(count>0):
    print(count)
    count=count-1



# Else with While Loop
# We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.
    
#Example:
count=5
while(count>0):
    print(count)
    count=count-1
else:
    print("I am inside else")



