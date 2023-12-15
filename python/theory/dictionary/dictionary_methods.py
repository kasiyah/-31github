# Dictionary Methods

myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}

# clear()
# syncdax: dictionary.clear()
myDict.clear()
print(myDict)

# copy() 
# returns a shallow copy of dictionary. It does not modify the original dictionary.
# when the method is called a new dictionary is created
# syncdax: dictionary.copy()
myDict2 = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
dict = myDict2.copy()
print(myDict2)
print(dict)
