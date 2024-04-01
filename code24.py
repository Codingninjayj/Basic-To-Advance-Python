# Python Tuples
# Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

# Example 1:
tup=(1,2,3,"yash",True)
print(type(tup),tup)
print(len(tup))

# Tuple Indexes
# Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.

# Example:
print(tup[0])

# Accessing tuple items:
# I. Positive Indexing:
# As we have seen that tuple items have index, as such we can access items using these indexes.
# Example:
print(tup[2])
print(tup[3])

# II. Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

# Example:
print(tup[-1])

# III. Check for item:
# We can check if a given item is present in the tuple. This is done using the in keyword.

# Example 1:
if 2 in tup:
    print("yes 2 is present in tuple")

#Slicing of tuple:
tup2=tup[1:4]
print(tup2)