Arrays - not native DS in Python (list is native to Python)
- is a DS which can store collection of elements of the same type
- store elements as contigious blocks of memory without pointers, reducing memory overhead.
- can only store elements of the same data type
- each element has a unique index

Types of Arrays
One Dimensional - linear array
Multi Dimensional
2D --> i[row index][column index]
3D --> i[depth index][row index][column index]

Types of Arrays in Memory
1D - compiler allocates 9 contiguous cells in memory, all cells next to each other. It can start in any location.
2D - in memory it is represented as one dimensional array
3D - in memory it is represented as one dimensional array

Common Operations that can be performed on Arrays

Array Module 
- more memory efficient than list for storing the large types of the same data type.
- supports only basic data types
- homogeneous (only same data types)
- import array
my_array = array.array('i')  --> i - denotes type of element integers

Numpy Module
- advantage: provides a feature rich and high performance array object, supports wide range of numerical operations and functions
- disadvantage: not part of Python standard library, you have to install additional library to be able to use it.
- import numpy
np_array = np.array([], dtype=int)

Time Complexity
- creating empty array ---> involves minimal operations such as initializing array metadata and allocating minimal 
amoount of memory for the array elements --> Time Complexity: O(1), Empty array has no elements, memory used for 
array metadata is constant and does not depend on the number of elements ---> Space Complexity: O(1)
- creating array with elements ---> involves copying elements from the input iteratively ---> Time Complexity: O(1), 
the memory allocation for the array elements depends on the number and the data type of the elements. As the number 
of elements increases, the memory needed to store those elements also increases proportionally. ---> Space Complexity: O(1)

Insertion to Array
my_array.insert(index, value) - this will insert needed value and shift indexes for other elements if needed.
Time complexity: depends on the number of elements that need to be shifted ---> O(N)
Space Complexity: when we are inserting into the array we need only one space for that element ---> O(1)

Array Traversal 
- visiting all cells of the array. Eg: printing elements one by one, or updating given element.
Time Complexity: we use for loop to traverse array --> O(n)
Space Complexity: we don't need extra location to perform traverse operation --> O(1)

Access Array Element 
- print value of cell number
arrayName[index] = "value"

def accessElement(array, index): 
    if index >= len(array): ---------------------------------------> O(1)
          print('There is no element with such index') ------------> O(1)
    else:
          print(array[index]) -------------------------------------> O(1)

Time Complexity:  because we just access element at certain index --> O(1)
Space Complexity: we do not need extra space for this operation --> O(n)

Searching for and Element in Array
Linear Search 
- iterate through elements of the array one by one, comparing each element with the target value. If the target value is found, the search is successful and you can go ahead and return the index of the target value. If the target value is not found after iterating the all elements, the search is unsuccessful and you can return an indication that the value was not found.

def linearSearch(arr, target):
    for i in range(len(arr)): --------------------------------------> O(n)
        if arr[i] == target: ---------------------------------------> O(1)
            return i  ----------------------------------------------> O(1)
        return -1     ----------------------------------------------> O(1)

Time Complexity:  total time complexity --> O(1)
Space Complexity: we do not need extra space for this operation --> O(1)

Deleting an Element from Array
- deletion is very efficient when you remove the last element, otherwise it becomes time consuming.
Time Complexity: o(n)
- if remove just last element - O(1)
- if removing any other element we need to shift following elements one step left - O(n) - worst case
Space Complexity: O(1)
- we are not taking any extra space when deleting

Time and Space Complexity of Array

Operation                       | Time Complexity | Space Complexity
---------------------------------------------------------------------
Creating empty array            |  O(1)           |   O(1)
Creating an array with elements |  O(n)           |   O(n)
Inserting value in array        |  O(n)           |   O(1)
Traversing a given array        |  O(n)           |   O(1)
Accessing a given array         |  O(1)           |   O(1)
Searching a given value         |  O(n)           |   O(1)
Deleting a given value          |  O(n)           |   O(1)


-------------------------------------------------------------------------------------------------