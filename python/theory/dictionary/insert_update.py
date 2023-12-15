# Insert/Update an element in a Dictionary
# Dictionaries are mutable. We can add new items or change the value of existing item using the assignment operator.
# If the key is already present the value gets updated. Otherwise the new key-value pair is added to the dictionary. 

# Update an element of the Dictionary 
myDict = {'name': 'Edy', 'age': 26}
myDict['age'] = 27
print(myDict)

# Time Complexity: O(1) 
# We are accessing key and changing its value, we do not do any looping or searching

# Space Complexity: O(1)
# Extra memory is not required
##################################


# Add an element to the Dictionary
myDict['address'] = 'London'
print(myDict)

# Time Complexity: O(1) 
# We are just adding key and value

# Space Complexity: amortized O(1)
# In most cases it's O(1). It changes to O(n) when underlying data structure needs to grow or shrink.
# As the latter only happens infrequently people use the word amortized. 
# Eg: If we add pairs to the dictionary and the capacity of dictionary is reached, the space allocation id doubling. 