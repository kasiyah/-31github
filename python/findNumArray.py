# Question 3 - How to check if an array contains a number in Python

import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def findNumber(arr, target):
    index = 0
    for i in range(len(arr)):
        if arr[i] == target:
            print('Index: ' + str(i))
            index = 1
    
    if index == 0:
        print('Number not found in the array')


findNumber(myArray, 170)