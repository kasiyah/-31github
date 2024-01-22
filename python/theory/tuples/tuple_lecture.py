### Tuples 

# What is Tuple?
# 
# 
# 
# 
# 

# Syntax of creating tuples
# my_tuple = 1,2,2,3
# my_tuple = (1,2,2,3)

# How to create a Tuple?
my_tuple = (1,2,2,3)
print(my_tuple)
# comma
my_tuple1 = ('abe',)
# tuple()
    # my_tuple2 = tuple()
my_tuple3 = tuple('abcde')
print(my_tuple3)
# tuple() constcructor
tuple1 = tuple()
print(tuple1)
# Time Complexity:O(1)
# Space Complexity:O(n)

# Tuples in Memory
# 
# 

######################################
# Accessing elements of Tuple:
# use bracket operator like for lists 
print(my_tuple[2])
# negative index 
print(my_tuple[-1])
# slice [:] operator
print(my_tuple[:2])
######################################
# Traversing a Tuple
# for loop
for i in my_tuple:
    print(i)
# for loop with range
for i in range(0, len(my_tuple)):
    print(my_tuple[i])
# Time Complexity: O(n)
# Space Complexity: O(1)

######################################
# Search Element in Tuple
# in operator
print(1 in my_tuple)
# index method
print(my_tuple.index(2))
# custom message
def searchTuple(p_tuple, element):
    for i in range(0,len(p_tuple)):
        if p_tuple[i] == element:
            return f"The {element} element is found at index {i}."
    return f"The {element} element is not found."

print(searchTuple(my_tuple, 4))
######################################
# Tuple Operators
# Concatenation Operator
my_tuple2 = (4,5,6)
print(my_tuple + my_tuple2)
# Star Operator
print(my_tuple * 3)
# in Operator
print(7 in my_tuple)
######################################
# Tuple Methods

# Count Method
print(my_tuple.count(2))
# Index method

######################################
#Tuple Functions
# len Function
# max Function
# min Function
# tuple method
print(tuple([1,2,3,4]))

##########################################
#Lists VS Tuples
#
my_tuple = (7,8,9,10,11)
print(my_tuple)
#
del my_tuple
print(my_tuple)
#
#
#