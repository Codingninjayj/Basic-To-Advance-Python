# What are strings?
# In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

# Example: method 1

name = "Yash"
print("Hello, " + name) #Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.
 
# method:2
#it can print anything which comes under 3 comma or 2
fri='''hi,my name is rahul''' 
print(fri)

# Accessing Characters of a String
# In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
# Square brackets can be used to access elements of the string.

#Example:
print(name[1])
print(fri[4])
# print(name[5]) This thowrs an error Because the strings end.

# Looping through the string
# We can loop through strings using a for loop like this:

for b in name:
    print(b)