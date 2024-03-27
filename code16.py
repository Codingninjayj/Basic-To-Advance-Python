# Introduction to Loops
# Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

# for loop
# while loop

# The for Loop
# for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

#Example:
name="yash"
for i in name:
    print(i)
    if(i=="h"):
        print("this is spmthing special")

#Example 2:
Colours =["red","Green","Blue","Yellow"]
for color in Colours:
    print(color)
    for i in color:
        print(i)


# range():
# What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

# Here, we can use the range() function.
#Example 1:
for i in range(5):
    print(i+1)

#Example 2:
for k in range(1,9):
    print(k)

#Example 3:
for k in range(1,9,1):
    print(k)