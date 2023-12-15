Two Dimensional Arrays
- an array with a bunch of values having been declared with double index - arr[i][j]
- use 2D array when you have to deal with matrix

When we create an array, we:
- assign it to a variable
- define the types of elements that it will store
- define its size (the max numbers of elements) <--- might not be needed in some languages

Creating Two Dimensional Array:
import numpy as np
 
twoDArray = np.array([[11,15,10,16],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)

Time complexity of creating a 2D array - O(m*n) ---> m - number of columns, n - number of rows
Space complexity of creating a 2D array - O(m*n) ---> m - number of columns, n - number of rows. 
So we need this much of space in the memory.

Insertion - Two Dimensional Array
Addition of Columns:
- adding a column at the beginning of 2D array - column will be inserted in index 0, other columns shift one step right
- time complexity: O(m*n)

Addition of Rows:
- adding a row at the beginning of a 2D array - row will will inserted in index 0, other rows will be shifted one step down
- time complexity: O(m*n)



import numpy as np
 
twoDArray = np.array([[11,15,10,16],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)
 
#Inserting row or column
newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=1)
print(newTwoDArray)
 
#Appending row or column 
#Index is not needed as it always inserts at the end of array
newTwoDArray1 = np.insert(twoDArray,[[1,2,3,4]], axis=0)
print(newTwoDArray1)

- 0 - index of where you want to insert
- axis - to denote if its column (axis=1) or row (axis=0)
Time complexity: O(m*n)


"Access an Element of Two Dimensional Array"

array[i][j] - i is row, j is column

import numpy as np
 
twoDArray = np.array([[11,15,10,16],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)
 
def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]): #---> O(1)
        print('Incorrect index')  #------------------------------> O(1)
    else:
        print(array[rowIndex][colIndex]).  #---------------------> O(1)
 
accessElement(twoDArray,1,2)

Time complexity: O(1)
Space complexity: O(1)



"Traversal Two Dimensional Array"

import numpy as np
 
twoDArray = np.array([[11,15,10,16],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)

def traverseTDArray(array):
    for i in range(len(array)):  # ------------------> O(mn) for each row we have to traverse all the columns
        for j in range(len(array[0])): #-------------> O(n)
            print(array[i][j])  #--------------------> O(1)
 
traverseTDArray(twoDArray)

Time complexity: O(m*n) --> if m==n --> O(n^2)
Space complexity: O(1)


"Searching Two Dimensional Array"

import numpy as np
 
twoDArray = np.array([[11,15,10,16],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)
 
def serachTDArray(array, value):
    for i in range(len(array)):  # ------------------> O(mn) for each row we have to traverse all the columns
        for j in range(len(array[0])): #-------------> O(n)
            if array[i][j] == value:   #-------------> O(1)
                return 'The value is located at index '+str(i)+""+str(j)
    return 'The elemenet is not found'
 
print(serachTDArray(twoDArray, 14))

Time complexity: O(m*n) --> if m==n --> O(n^2)
Space complexity: O(1)


"Deletion in 2D array"
In numpy we are not straightway deleting column/row from array. We are copying the original data without deleted column into a new array.

import numpy as np
 
twoDArray = np.array([[11,15,10,16],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)
 
#This deletes the first row(axis=0) 
newTDArray = np.delete(twoDArray, 0, axis = 0)
print(newTDArray)

Time complexity: O(m*n)
Space complexity: O(m*n)



Time and Space Complexity of 2D Array

Operation                       | Time Complexity | Space Complexity
---------------------------------------------------------------------
Creating empty array            |  O(1)           |   O(1)
Creating an array with elements |  O(mn)          |   O(mn)
Inserting value in array        |  O(mn)          |   O(mn)
Traversing a given array        |  O(mn)          |   O(1)
Accessing a given array         |  O(1)           |   O(1)
Searching a given value         |  O(mn)          |   O(1)
Deleting a given value          |  O(mn)          |   O(mn)


When to use/avoid Arrays

When to use:
- to store multiple variable of the same datatype
- random access

When to avoid:
- different data type elements --> if you want to declare variables of different data types, 
so for each data type we need to create separate arrays.
- array reserves memory --> Maybe it reserves a memory that will not be used in the future, 
but it takes a memory in our RAM. This also causes another problem when you add elements 
to an array and array begins to exceed its reserves capacity. In this case, the array allocates
a larger region of memory and copies its elements into the new storage.
