def check_same_frequency(list1, list2):
    # TODO
    word_count1 = {}
    word_count2 = {}
    for word in list1:
        word_count1[word] = word_count1.get(word, 0) + 1
    for word in list2:
        word_count2[word] = word_count2.get(word, 0) + 1  
    return word_count1 == word_count2

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))

"""
SOLUTION - Time and Space Complexity of Same Frequency
def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter
    
    return count_elements(list1) == count_elements(list2)
Explanation:


check_same_frequency(list1, list2)  checks if two given lists have the same frequency of elements.

Define an inner function count_elements(lst) that counts the frequency of elements in a list lst. 
The function creates an empty dictionary counter, iterates through the list, and increments the 
count for each element using the get() method. The get() method takes O(1) average time complexity. 
The function returns the counter dictionary. 
The time complexity of count_elements() is O(n), where n is the number of elements in the input list lst. 
The space complexity is also O(n), as the dictionary counter has as many keys as there are distinct elements in the list.

Call the count_elements() function on both input lists list1 and list2. 
This operation has a time complexity of O(n1 + n2), where n1 and n2 are the lengths of list1 and list2, respectively. 
The space complexity is O(m1 + m2), where m1 and m2 are the numbers of distinct elements in list1 and list2, respectively.

Compare the resulting dictionaries using the == operator. This operation has a time complexity of O(min(m1, m2)), 
as it compares the keys and values of both dictionaries.

Return the result of the comparison (True if the dictionaries are equal, False otherwise).

Time complexity:
The overall time complexity of this function is O(n1 + n2 + min(m1, m2)), where n1 and n2 are the lengths 
of list1 and list2, and m1 and m2 are the numbers of distinct elements in list1 and list2, respectively. 
This is determined by the time complexity of the count_elements() function and the dictionary comparison.

Space complexity:
The space complexity of this function is O(m1 + m2), where m1 and m2 are the numbers of distinct elements 
in list1 and list2, respectively. This is because the function creates two dictionaries with as many keys 
as there are distinct elements in the input lists.
"""