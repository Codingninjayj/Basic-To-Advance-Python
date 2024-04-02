# f-strings in python
# It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

# When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

# Example

letter="hey my name is {} and i am from {} "
country="India"
name ="yash"

# print(letter.format(name,country))
print(f"hey my name is {name} and i am from {country} ")

# String formatting in python
# String formatting can be done in python using the format method.
#Example::

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.21345 ))

# We can use it in a single statement as well.

# Example
print(f"{2*30}")