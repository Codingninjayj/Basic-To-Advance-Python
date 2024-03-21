# Variables and Data Types
# What is a variable?
# Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:

# example::
a=1
print(a)
b="yash" # To represent the charachter in variable we use " " semi coln.
print(b)

# What is a Data Type?
# Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
# In python, we can print the type of any operator using type function:

#types of data types::
# 1. Numeric data: int, float, complex
# int: 3, -8, 0
# float: 7.349, -9.0, 0.0000001
# complex: 6 + 2i


# 2. Text data: str
# str: "Hello World!!!", "Python Programming"


# 3. Boolean data:
# Boolean data consists of values True or False.



a=1
b="yash"
c=True
d=None
e=complex(2,1)
print(a)
print(b)
a1=9
print(a+a1)
# type() this command is used to find which type of data type  is the given in the variable
print("This type is a is",type(a))
print("This type is b is",type(b))
print("This type is c is",type(c))
print("This type is d is",type(d))
print("This type is e is",type(e))

""""
4. Sequenced data: list, tuple
list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

Example:

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

Output:

[8, 2.3, [-4, 5], ['apple', 'banana']]

example::
"""

list1=[8,5,7,[-4,5],["apple","banna"]]
print(list1)

tuple1=(("parrot","sparrow"),("lion","tiger"))
print(tuple1)


'''
Mapped data: dict
dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets

'''
dict1={"name":"Sakshi","age":20,"canvote":True}
print(dict1)



