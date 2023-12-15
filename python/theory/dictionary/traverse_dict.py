# Traversing through a dictionary


myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

def traversDict(dict):
    for key in dict:    #-------------------------------------------> O(n)
        print(key, dict[key])     #---------------------------------> O(1)

traversDict(myDict)



# Time Complexity: O(n) 

# Space Complexity: O(1)
# Extra memory is not required, we are just traversing through existing key-value pairs
