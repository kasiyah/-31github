# Traversing a Tuple

new_tuple = ('a', 'b', 'c', 'd', 'e')
# for loop
for i in new_tuple:
    print(i)
 
# range
for i in range(len(new_tuple)):
    print(new_tuple[i])

# Time Complexity: O(n) - because we visit each element
# Space Complexity: O(1) - because additional memory is not required

# Search Element in Tuple
# in operator
print('a' in new_tuple)
# index method
print(new_tuple.index('c'))
# custom message
def searchTuple(p_tuple, element):
    for i in range(0,len(p_tuple)):
        if p_tuple[i] == element:
            return f"The {element} element is found at index {i}."
    return f"The {element} element is not found."

print(searchTuple(new_tuple,'d'))

# Tuple Operators
# Concatenation Operator
myTuple = (1,2,3,4,5,2)
myTuple1 = (6,7,8,9)
print(myTuple + myTuple1)
# Star Operator
print(myTuple * 4)
# in Operator
print(4 in myTuple)

# Tuple Methods
# Count M3thod
print(myTuple.count(2))
# Index method
print(myTuple.index(2))

#Tuple Functions
# len Function
print(len(myTuple))
# max Function
print(max(myTuple))
# min Function
print(min(myTuple))
# tuple method
print(tuple([1,2,3,4]))

Tuple VS List

List is mutable, tuple is immutable.

list1 = [0, 1, 2, 3, 4, 5, 6, 7]
# reassign 2nd element
list1[1] = 3
# In the output you see that the element has changed
print(list1)
# reassign the whole list
list1 = [7, 6, 5, 4, 3, 2, 1]
# In the output you see that the whole list has been reassigned
print(list1)
tuple1 = 0, 1, 2, 3, 4, 5, 6, 7
# reassign 2nd element
tuple1[1] = 3
# In the output you see TypeError: 'tuple' object does not support item assignment
print(tuple1)
# reassign the whole tuple
tuple1 = 7, 6, 5, 4, 3, 2, 1
# In the output you see that the whole tuple has been reassigned
print(tuple1)


Once you declare a tuple you cannot change the element of tuple.
- We can reassign the whole tuple and list.
- We can reassign a single element in list, BUT we cannot reassign a single element in tuple.
- We can use a slice operator to delete elements from list, BUT we cannot use the slice operator to delete elements in tuple. We can only access element of tuple using slice operator.
- We can delete the entire tuple using del operator, but we cannot use it to delete single element of a tuple.

Functions:
- There are a lot of built-In functions that can be used for both tuples and list:
len()
max()
sum()
any ()
sorted()

Methods:
List and tuples share some methods.
index[] and count90 can used for both list and tuple
There are a few methods that apply to list only:
append()
insert()
remove()
pop()
clear()
sort()
reverse()



- Tuples can be stored in Lists
list1 = [(1, 2),(3, 4),(5, 6)]
print(list1)

- Lists can be stored in Tuples
tuple1 = ([1, 2],[3, 4],[5, 6])
print(tuple1)

- both Tuples and Lists can be nested
list1 = [[1, 2],[3, 4],[5, 6]]
print(list1)
tuple1 = ((1, 2),(3, 4),(5, 6))
print(tuple1)

- We generally use tuples for heterogeneous data types and list for homogeneous data types.
- Since tuples are immutable, iterating through a tuple is faster than with list ---> performance boost.
- Tuples that contain immutable elements can be used as a key for a dictionary, while with list this is not possible.
- If you have the data that does not change, implementing it as a tuple will guarantee that it remains write-protected, so no one can change it.