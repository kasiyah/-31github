# Accessing elements of Tuple:

new_tuple = ('a', 'b', 'c', 'd', 'e')
# use bracket operator like for lists
print(new_tuple[1])   # outputs b
 
#negative index also works in tuple. It starts from the right and outputs the last element in the tuple
print(new_tuple[-1])   # outputs e
 
# slice [:] operator
# syntax: tuple[leftIndex : rightIndex]
# the search will start from the left index to the right. The right index is not included here
print(new_tuple[1:3])   # output: ('b', 'c') - index 3 is not included
print(new_tuple[1:])    # outputs from index 1 till the end
print(new_tuple[:])     # will print all elements if the tuple

# Tuples are immutable ---> not able to update a tuple