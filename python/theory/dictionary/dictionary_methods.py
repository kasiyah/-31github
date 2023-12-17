# Dictionary Methods

# clear()
# syncdax: dictionary.clear()
print('\nclear() method:')
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
myDict.clear()
print(myDict)

# copy() 
# returns a shallow copy of dictionary. It does not modify the original dictionary.
# when the method is called a new dictionary is created
# syncdax: dictionary.copy()
print('\ncopy() method:')
myDict2 = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
dict = myDict2.copy()
print(myDict2)
print(dict)

# fromkeys()
# creates new dictionary from given sequence of elements with values provided by user
# returns a new dictionary with the given sequence of elements as the key of dictionary
# syntax: dictionary.fromkeys(sequence[],value)
print('\nfromkeys() method:')
newDict = {}.fromkeys([1,2,3])
print(newDict)

# get() method
# retunrs the value of the specified key if the key is in the dictionary
# maximum takes two parameters: key and value (optional. to be returned if the key is not found)
# 1. If the key is found ----> returns actual value
# 2. If the key is not in the dictionary and the values is not specified -----> returns None
# 3. If the key is not in the dictionary and the values is specified  -----> it returns the value spacified
# syncdax: dictionary.get(key,value)
print('\nget() method:')
myDict3 = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict3.get('age',27))
print(myDict3.get('city',27))
print(myDict3.get('city'))

# items()
# returns a view object that displays a list of dictonaries, key value tuple pairs
# it does not take any parameters
# syncdax: dictionary.items()
print('\nitems() method:')
myDict4 = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict4.items())


# keys()
# returns a view object that displays a list of all keys in the dictionary
# when dictionary changes the keys() method also reflects this change
# syncdax: dictionary.keys()
print('\nkeys() method:')
myDict5 = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict5.keys())

# popitem()
# returns an arbitrary element pair from the dictionary and removes that arbitrary element
# it does not takes any parameters
# syncdax: dictionary.popitem()
print('\npopitem() method:')
myDict6 = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict5.popitem())
print(myDict6)

# setdefault()
# returns the value of the key if the key is in the dictionary.
# if not it inserts a key with a value to the dictionary
# syncdax: dictionary.setdefault(key, default_value)
print('\nsetdefaul() method:')
myDict7 = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict7.setdefault('name1','added'))
print(myDict7)

# pop()
# returns and removes and elements from the dictionary having the given key
# syncdax: dictionary.pop(key, default_value)
print('\npop() method:')
myDict8 = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict8.pop('name1','not'))

# values()
# returns a view object that displays a list of all values in the dictionary
# syncdax: dictionary.values()
print('\nvalues() method:')
myDict9 = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict9.values())

# update()
# updates te dictionary with the elements from another dictionary obejct of from an iterable of key value paris
# adds elements to the dicrionary if the key is not in the dictionary
# if the key is in the dictionary it updates the key with the new value
# syncdax: dictionary.update(other_dictionary)
print('\nupdate() method:')
myDict10 = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
newDict1 = {'a':1, 'b':2, 'c':3}
print(myDict10.update(newDict1))
print(myDict10)








