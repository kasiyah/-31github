from array import *

# 1. Create an array and traverse
my_array = array('i',[1,2,3,4,5])
for i in my_array:
    print(i)

# 2. Access individual elements through indexes
print ('\nStep 2')
print(my_array[3])

# 3. Append any valueto the array using append() method
print ('\nStep 3')
my_array.append(6)
print(my_array)

# 4. Insert value in an array using insert() method
print ('\nStep 4')
my_array.insert(3, 11)
print(my_array)

# 5. Extend python array using extend() method
print ('\nStep 5')
my_array1 = array('i', [10,11,12])
my_array.extend(my_array1)
print(my_array)

# 6. Add items from list into array using fromlist() method
print ('\nStep 6')
templist = [20,21,22]
my_array.fromlist(templist)
print(my_array)

# 7. Remove any array element using remove() method 
print ('\nStep 7')
my_array.remove(11)
print(my_array)

# 8. Remove last array element using pop() method
print ('\nStep 8')
my_array.pop()
print(my_array)

# 9. Fetch any element through its index using index() method
print ('\nStep 9')
print(my_array.index(21))

# 10. Reverse a python array using reverse() method
print ('\nStep 10')
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method
# This method provides the arry buffer start address in the memory
# as well as the number of elements on the array
print ('\nStep 11')
print(my_array.buffer_info())

# 12. Check for number of occurences of an elememnt using count() method
# Counts the occurence of element
print ('\nStep 12')
my_array.append(11)
print(my_array.count(11))
print(my_array)

# 13. Convert array to string using tostring() method
print ('\nStep 13')
strTemp = my_array.tostring() #method depricate since Python 3.2
print(strTemp)
ints = array('i')
ints.fromstring(strTemp)
print(ints)

# 14. Convert array to a python list wih sam elements using tolist() method
print ('\nStep 14')
#print(my_array.tolist())

# 15. Append a string to char array using fromstring() method
# Shown as part of Step 13
print ('\nStep 15')

# 16. Slice elements from an array
print ('\nStep 16')
print(my_array[1:4])
