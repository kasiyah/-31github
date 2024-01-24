# Insert/Update an element in a Dictionary
# Dictionaries are mutable. We can add new items or change the value of existing item using the assignment operator.
# If the key is already present the value gets updated. Otherwise the new key-value pair is added to the dictionary. 

##################################
# Update an element of the Dictionary 
##################################
myDict = {'name': 'Edy', 'age': 26, 'education': 'masters'}
myDict['age'] = 27
# Time Complexity: O(1) - We are accessing key and changing its value, we do not do any looping or searching
# Space Complexity: O(1) - Extra memory is not required
print(myDict)

##################################
# Add an element to the Dictionary
##################################
myDict['address'] = 'London'
# Time Complexity: O(1) - We are just adding key and value
# Space Complexity: amortized O(1). In most cases it's O(1). It changes to O(n) when underlying 
# data structure needs to grow or shrink. As the latter only happens infrequently people use the word amortized. 
# Eg: If we add pairs to the dictionary and the capacity of dictionary is reached, the space allocation id doubling. 
print(myDict)

##################################
# Traversing through a dictionary
##################################
def traversDict(dict):
    for key in dict:    #-------------------------------------------> O(n)
        print(key, dict[key])     #---------------------------------> O(1)
# Time Complexity: O(n) 
# Space Complexity: O(1) - Extra memory is not required, we are just traversing through existing key-value pairs
print("\nTraverse Dictionary:")
traversDict(myDict)

##################################
# Find element in a dictionary
# Linear serach
##################################
def searchDict(dict,value):
    for key in dict:    #-------------------------------------> O(n)
        if dict[key] == value:    #---------------------------> O(1)
            return key, value     #---------------------------> O(1)
    return 'The value does not exist'  #----------------------> O(1)
# Time Complexity: O(n) 
# Space Complexity: O(1)- Extra memory is not required, we are just traversing through existing key-value pairs
print("\nSearch element: ")
print(searchDict(myDict, 26))

##################################
# Delete element from a dictionary
##################################
# del() method
del myDict['age']
print("\ndel() method: ")
print(myDict)
# Time Complexity: O(1) - It uses hash table operation
# Space Complexity: O(1) - It does not create any additional data structure to complete this operation. 

# pop() method
removed_element = myDict.pop('address')  # provide None is the key is not found in the dict. Eg myDict.pop('Num', None) 
print(removed_element)
print("\npop() method: ")
print(myDict)
# Time Complexity: O(1) - It uses hash table operation
# Space Complexity: O(1) - It does not create any additional data structure to complete this operation. 

#popitem() method
removed_element1 = myDict.popitem()  # provide None is the key is not found in the dict. Eg myDict.pop('Num', None) 
print(removed_element1)
print("\npopitem() method: ")
print(myDict)
# Time Complexity: O(1) 
# Space Complexity: O(1)

# clear() method - removes all key value pairs from the dictionary leaving it empy
myDict2 = {'name': 'Sarah', 'age': 21, 'address': 'New York', 'education': 'bachelors'}
print("\nclear() method: ")
print(myDict2)
myDict2.clear()
print(myDict2)
# Time Complexity: O(n) - Beause it has to remove all n elements from the dictionary
# Space Complexity: O(1)
