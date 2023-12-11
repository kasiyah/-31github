# Find the maximmum product of two integers in an array where elements are postitive.
# Ex: arr = [1, 7, 3, 4, 9, 5]
# max_product(arr)
# Output: 63 (9*7)

def max_product(arr):
    # arr.sort(reverse=True)
    # return arr[0]*arr[1]
    max1, max2 = 0, 0
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1*max2

arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))


"""
def max_product(arr):
Define a function named max_product that takes an input array arr.

max1, max2 = 0, 0
Initialize two variables, max1 and max2, to store the two largest numbers in the array. 
Set both variables to 0 initially.

for num in arr:
Iterate through the elements of the input array arr using a for loop. 
num represents the current element of the array.

if num > max1:
Check if the current number num is greater than the current maximum value max1.

max2 = max1
If the condition in line 4 is True, update the second-largest number max2 
by assigning it the value of the current largest number max1.

max1 = num
Update the largest number max1 by assigning it the value of the current number num.

elif num > max2:
If the condition in line 4 is False, check if the current number num is greater 
than the current second-largest number max2.

max2 = num
If the condition in line 7 is True, update the second-largest number max2 
by assigning it the value of the current number num.

return max1 * max2
After the loop has finished iterating through the array, return 
the product of the two largest numbers, max1 and max2.



Time Complexity:
The time complexity of the max_product function is O(n), where n is the length of the input array arr. 
The reason for this complexity is that the function iterates through the input array once, 
comparing each element with max1 and max2 to find the two largest elements. There are no nested loops 
or other time-consuming operations, so the time complexity is linear.

Space Complexity:
The space complexity of the max_product function is O(1), which means it uses a constant amount of extra memory 
regardless of the input size. In this case, the function uses two additional variables, max1 and max2, 
to store the two largest numbers in the array. No other data structures or memory allocations are required, 
so the space complexity remains constant regardless of the size of the input array.
"""