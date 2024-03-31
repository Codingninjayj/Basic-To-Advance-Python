# Python Functions
# A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

# There are two types of functions:

# Built-in functions
# User-defined functions

# Built-in functions:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

#Example1:
# a=2
# b=4
# gmean1=(a*b/(a+b))
# print(gmean1)


# User-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

#Example2:
def calculategmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def greaternumber (a,b):
 if(a>b):
    print("first number is greater")
 else:
    print("second number is greater")

def lessernumber(a,b):
   pass #this is used to pass the statement without getting any error and can be changed later.
a=10
b=12
greaternumber(a,b)
calculategmean(a,b)  

#Calling a function:
# We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

# Example:

# def name(fname, lname):
#     print("Hello,", fname, lname)

# name("Sam", "Wilson")

