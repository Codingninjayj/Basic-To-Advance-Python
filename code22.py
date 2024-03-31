# List Methods
# list.sort()
# This method sorts the list in ascending order. The original list is updated

# Example 1:
l=[1,5,6]
A=[1,2,4]
Ascend=[11,1,12,3,2,1]
In=[1,5,7,1,9,2]
print(l)

# append():
# This method appends items to the end of the existing list.
# Example 2:
A.append(7) 
print(A)

# Example 3:
Ascend.sort()
print(Ascend)

#For decsending order 
l.sort(reverse=True)
print(l)


# reverse()
# This method reverses the order of the list.
# Example:
A.reverse()
print(A)

# index()
# This method returns the index of the first occurrence of the list item.
# Example:
print(In.index(2))

# count()
# Returns the count of the number of items with the given value.
print(In.count(1))

# copy()
# Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

# Example:
m=In.copy()
m[0]=0
print(In)
print(m)

# insert():
# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

# Example:
m.insert(1,45)
print(m)

# extend():
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

# Example 1:
n=[900,1100,1000]
m.extend(n)
print(m)

# Concatenating two lists:
# You can simply concatenate two lists to join two lists.
# Example:
k=m+n
print(k)
