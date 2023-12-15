# Delete element from a dictionary

myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}

# del() method
del myDict['age']
print(myDict)

# Time Complexity: O(1) 
# It uses hash table operation

# Space Complexity: O(1)
# It does not create any additional data structure to complete this operation. 

# pop() method
removed_element = myDict.pop('address')  # provide None is the key is not found in the dict. Eg myDict.pop('Num', None) 
print(removed_element)
print(myDict)

# Time Complexity: O(1) 
# It uses hash table operation

# Space Complexity: O(1)
# It does not create any additional data structure to complete this operation. 

#popitem() method
removed_element1 = myDict.popitem()  # provide None is the key is not found in the dict. Eg myDict.pop('Num', None) 
print(removed_element1)
print(myDict)
# Time Complexity: O(1) 
# Space Complexity: O(1)


# clear() method - removes all key value pairs from the dictionary leaving it empy
myDict2 = {'name': 'Sarah', 'age': 21, 'address': 'New York', 'education': 'bachelors'}
print(myDict2)
myDict2.clear()
print(myDict2)
# Time Complexity: O(n) 
# Beause it has to remove all n elements from the dictionary
# Space Complexity: O(1)
