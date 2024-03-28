# break statement
# The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

#Example:
for i in range(12):
    if(i==10):
        break
    print("5 x",i+1, "=",5*(i+1))
print("exited the loop")


# Continue Statement
# The continue statement skips the rest of the loop statements and causes the next iteration to occur.

# example 2:
for i in range(12):
    if (i == 10):
        print("Skip the itration")
        continue
    print("5 x",i,"=",5*i)s
print("Exited the loop")


# Do-While loop in python
# do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

# How to emulate do while loop in python?
# To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

# The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:

#Example:
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break

    