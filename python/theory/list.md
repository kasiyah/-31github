"Python List"
- a DS that holds ordered collection of items
- the place of elements does not change
- elements don't have to be of the same type

integers = [1,2,3,4]
print(integers)
 
stringList = ['Milk', 'Cheese', 'Butter']
print(stringList)
 
mixedList = [1, 1.2, 'spam']
print(mixedList)
 
nestedList = [1,2,3,4,[1.5,1.6],[test]]
print(nestedList)
 
emptyList = []
print(emptyList)



"Accessing/Traversing the List"
#Accessing element
shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[0])
 
#Accessing element, starts from the back of the list with -1
print(shoppingList[-2])
 
#Checks if element exists in list
print('Milk' in shoppingList)
 
#Traverse list
for i in shoppingList:
    print(i)
 
#Traverse and update the list
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(i)


"Update/Insert into the List"

"Updating List"

myList = [1,2,3,4,5,6,7]
print(myList)
 
#Update element
myList[2] = 33
myList[3] = 55
print(myList)

Lists are ordered collections --> elements will be printed in the same order we declare them.
Time complexity: O(1)
Space complexity: O(1)


"Inserting an Element into the List"

myList = [1,2,3,4,5,6,7]
print(myList)
#Insert method, each element shifts to the right after insertion
myList.insert(0,11) #-----------------------------> O(n)
print(myList)
 
#append method, adds element at the end of list
myList.append(11)  #------------------------------> O(1)
print(myList)
 
#extend method, adds another list to existing list
newList = [11,12,13,14]
myList.extend(newList)  ##------------------------> O(n)
print(myList)



"Slice/Delete Element from List"

#Slice   
myList = ['a','b','c','d','e','f']
#prints elements index 0, until :2 ---> 2(-1)=1
print(myList[0:2])
#if you omit first index it prints elements until index :2
print(myList[:2])
#if you omit 2nd index it prints elements starting from 1st index :1 -->1(-1)=0
print(myList[1:])
#omitting both indexes prints all elements of the list
print(myList[:])
#updating using slice operator
myList[0:2] = ['x','y']
print(myList)

a=[1,2,3,4,5]
print(a[3:0:-1])
Explanation
The given code block performs a slice operation on the list a using the syntax a[start:stop:step]. In this case, start is 3, stop is 0, and step is -1. This slice operation creates a new list containing elements from the original list, starting at index 3, going until index 0 (not inclusive), and selecting every element with a step of -1 (moving in reverse).

So, the output of the code block will be:

csharpCopy code
[4, 3, 2]
The slice operation picks the elements at indices 3, 2, and 1 from the original list.




"Delete Element from List"

#pop method, returns popped element
#after element is popped, other element shift left one step
myList = ['a','b','c','d','e','f']
#deletes element index 1
print(myList.pop(1)) #----------------------------> O(n) - since other elements shift
#deletes last element
myList.pop() #------------------------------------> O(1) - if deleting the last element
print(myList)
 
#delete method, this function does not return anything
del myList[3] #-----------------------------------> O(n) - since other elements shift
print(myList)
 
del myList[2:4]
print(myList)
 
#remove method, removes element itself not index based
myList.remove('e')  #--------------------------- -> O(n) - since other elements shift
print(myList)


"Searching for an Element in a List"

#Searching for an element in thelist
myList = [10,20,30,40,50,60,70,80,90]
#in operator
target = 50
if in in myList: #--------------------------------> o(n) - goes through every element
    print(f"{target} is in the list")
else:
    print(f"{target} is NOT in the list")
 
#Linear Search
def linear_search(p_list, p_target):
    #enumerate function iterates through the list keeping track of the current index
    for i, value in enumerate(p_list):  #---------> O(n)
        if value == p_target:  #------------------> O(1)
            return i  #---------------------------> O(1)
        return -1  #------------------------------> O(1)
 
print(linear_search(myList,target))

Time complexity: O(n)
Space complexity: O(1)