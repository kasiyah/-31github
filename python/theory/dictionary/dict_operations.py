# In operator
# works only with keys not with values
print('\n"in" operator:')
myDict = {
    3: "three",
    5: "five",
    9: "nine",
    2: "two",
    1: "one",
    4: "four"
}
print(3 in myDict)

# to check if the value is in the dictionary
print("three" in myDict.values())

# len() fuction 
# it takes each pair as one element and returns the number of elements (pairs)
print('\n"len()" function:')
print(len(myDict))


# all() fuction 
# it checks keys of dictionary and if all keys in the dictionary are true it returns true
# if one of the keys is 0 it will return false
print('\n"all()" function:')
# 1. If all keys are true - returns true
print(all(myDict))
# 2. If all keys are false - returns false
myDict1 = {
    0: "zero", 
    False: "False"
}
print(all(myDict1))
# 3. If one key is true - returns false
myDict2 = {
    1: "zero", 
    False: "False"
}
print(all(myDict2))
# 3. If one key is false - returns false
myDict3 = {
    0: "three",
    5: "five",
    9: "nine",
    2: "two",
    1: "one",
    4: "four"
}
print(all(myDict3))

# any() fuction 
# 
print('\n"any()" function:')
# 1. If all keys are true - returns true
print(any(myDict))
# 2. If all keys are false - returns false
print(any(myDict1))
# 3. If one key is true - returns true
print(any(myDict2))
# 3. If one key is false - returns true
print(any(myDict3))

# sorted() fuction 
# returns list of keys of the dictionary in a sorted manner
print('\n"sorted()" function:')
print(sorted(myDict))
