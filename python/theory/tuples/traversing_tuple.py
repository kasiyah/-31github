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