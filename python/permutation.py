def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    #convert string into list
    list1 = list(list1)
    list2 = list(list2)
    #sorts list
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
#list1 = ['a', 'c', 'b']
#list2 = ['c', 'a', 'b']
list1 = "peek"
list2 = "keep"
print(permutation(list1,list2))