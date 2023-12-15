Dictionary

- collection which unordered, changeable, and indexed.
- we use key to associate with its value, any value can be identified as long as we know the key.

myDict = {"Miller" : "a person who owns or works in a corn mill", 
          "Programmer" : "a person who writes computer programs"}
myArray = ["Miller", "Programmer", "App Miller"]
Accessing elements:

myArray[0]            ---------------------------> Miller

myDict["Miller"]   ---------------------------> a person who owns or works in a corn mill

- for an array index positions should be integers
- for a dictionary key (index) can be any type


How to create a dictionary?
Dictionary

- a mutable collection of key value pairs where each unique key maps to the value.

- implemented using hash tables which provides fast access to values based on their keys.

# using dict() constructor
myDict = dict()
print(myDict)
 
#using curvy brackets {}
myDict2 = {}
print(myDict2)
Time Complexity: O(1)

Space Complexity: O(1) - as the dictionary is empty and the only memory for the initial hash table structure is allocated.

# when using dict() constructor we only need to specify data type of the value
# dict() constructor will automatically konvert key into string data type
eng_sp = dict(one='uno', two='dos', three='tres')
print(eng_sp)
 
# using curvy brackets
# we need to specify data type of key string here and use : 
eng_sp2 = {'one':'uno', 'two':'dos', 'three':'tres')
print(eng_sp2)
Time Complexity: O(n) - because each key and value pair need to be inserted in the dictionary ant it will take some time

Space Complexity: O(n)

# using dict() constructo and list of tuples
eng_sp_list = [('one','uno'), ('two','dos'), ('three','tres')]
eng_sp3 = dict(eng_sp_list)
print(eng_sp3)
