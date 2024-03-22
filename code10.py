#String are immutable
a="Yash!!!!!!"
print(len(a))

# this .upper() is used to captial every letter present in variable
print(a.upper()) 

# this .lower() is used to small every letter present in variable
print(a.lower()) 

#The strip() method removes any white spaces before and after the string.
print(a.rstrip("!"))

#The replace() method replaces all occurences of a string with another string.
print(a.replace("Yash","John"))

#The split() method splits the given string at the specified instance and returns the separated strings as list items.
print(a.split(" "))

# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
blog="this is to show how capitalize works"
print(blog.capitalize())

# The center() method aligns the string to the center as per the parameters given by the user.
print(blog.center(50))

# The count() method returns the number of times the given value has occurred within the given string.
print(blog.count("a"))

# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str1="Welcome to my proflie!!!"
print(str1.endswith("!"))
 
print(str1.endswith("to",4,10))

# The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
str2 = "He's name is Dan. He is an honest man."
print(str2.find("is"))

# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
print(str2.index("Dan"))


# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
str3="Welcometomyproflie"
print(str3.isalnum())

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
str4="YashJadhav"
print(str4.isalpha())

# The islower() method returns True if all the characters in the string are lower case, else it returns False.
str5="yash"
print(str5.islower())

# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
str6="happy  birthday"
print(str6.isprintable())

# str6="happy \n birthday"
# print(str6.isprintable()) this is not printable charater because of \n.


# The isspace() method returns True only and only if the string contains white spaces, else returns False.
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

# The isupper() method returns True if all the characters in the string are upper case, else it returns False.
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

# The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

# The title() method capitalizes each letter of the word within the string.
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())