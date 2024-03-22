#  Taking User Input in python
# In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable

# Syntax:
# variable=input()
#Example:
a=input("Enter your name:")
print("my name is ", a)

# But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

# Example:

x=int(input("Enter your first number:"))
y=int(input("Enter your second number:"))
print(x+y)

#method 2:
x=input("Enter your first number:")
y=input("Enter your second number:")
print(int(x)+int(y))