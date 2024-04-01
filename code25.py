# Manipulating Tuples
# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

# Example:
name=("yash","abhishek","rohan","Shrushti","charan")
temp=list(name) #convert tuple to list
temp.append("vivek") #add item
temp.pop(2) #remove item
temp[0]="jadhav" #Change item

name =tuple(temp)
print(type(name),name)

#Example 2:how to add two tuple :
name=("yash","jadhav")
name2=("ram","charan")
n=name+name2
print(n)


# Tuple methods
# As tuple is immutable type of collection of elements it have limited built in methods.They are explained below

# count() Method
# The count() method of Tuple returns the number of times the given element appears in the tuple.

# Example:
tuple1=(1,2,4,5,6,3,2,1,3,1,4,5,4)
res=tuple1.count(4)
print("Count of 4 in tuple1 is:",res)


# Index() method
# The Index() method returns the first occurrence of the given element from the tuple.
# res1=tuple1.index(6)
res1=tuple1.index(2,5,10)
print("Index value of 6 is :",res1)
print("lenght of tuple:",len(tuple1))#to find lenghth of tuple

