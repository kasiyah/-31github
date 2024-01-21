Tuples - a sequence of values, much like a list.
- values can be any type
- indexed by integers
- immutable sequence of Python objects (when we declare a tuple we cannot change it)
- comparable and hashable, so we can sort of list them and use tuples as key values in Python dictionary.

An object is set to be hashable if it has a value that remains the same during its lifetime.

Syntax of creating tuples:
t = 'a', 'b', 'c', 'd', 'e'
t = ('a', 'b', 'c', 'd', 'e') # to helpp us identify tuples when we look at python code


How to create a Tuple?
new_tuple = ('a', 'b', 'c', 'd', 'e')
print(new_tuple)
 
# when creating a tuple it is important to include comma after element
# otherwise it will not be a tuple, it will be a string
new_tuple1 = ('a',)
print(new_tuple1)
 
# built in tuple() function. 
# creates an empty tuple
new_tuple2 = tuple()
print(new_tuple2)

# creates a tuple from string making each character e separate tuple element
new_tuple3 = tuple('abcde')
print(new_tuple3)

Because the tuple is the name of constructor we always have to avoid using it as a variable name. Because in this case it might cause confusion.

Time Complexity: O(1) - because we are defining all elements upfront

Space Complexity: O(n) - because it depends on the n umber of elements of the tuple.


Tuples in Memory

- elements of tuple located in the memory contiguously
- unlike lists and arrays, tuple are immutable. Once you declare them you cannot change them. It stays as it is