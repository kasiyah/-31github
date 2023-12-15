# Find element in a dictionary
# Linear serach

myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

def searchDict(dict,value):
    for key in dict:    #-------------------------------------> O(n)
        if dict[key] == value:    #---------------------------> O(1)
            return key, value     #---------------------------> O(1)
    return 'The value does not exist'  #----------------------> O(1)

print(searchDict(myDict, 26))

# Time Complexity: O(n) 

# Space Complexity: O(1)
# Extra memory is not required, we are just traversing through existing key-value pairs
