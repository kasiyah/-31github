from linked_list import LinkedList

def sum_list(llA, llB):
    n1 = llA.head
    n2 = llB.head
    sum = LinkedList()
    carry = 0
    while n1.next and n2.next:
        n3 = n1.value + n2.value + carry
        if n3 > 0:
            carry = int(n3/10)
            n3 = n3 % 10
        sum.add(n3)
        n1 = n1.next
        n2 = n2.next
    n3 = n1.value + n2.value + carry
    sum.add(n3)
    return sum

# Solution
# def sum_list(llA, llB):
#     n1 = llA.head
#     n2 = llB.head
#     carry = 0
#     ll = LinkedList()
#     while n1 or n2:
#         result = carry
#         if n1:
#             result += n1.value
#             n1 = n1.next
#         if n2:
#             result += n2.value
#             n2 = n2.next
#         ll.add(int(result % 10))
#         carry = int(result / 10)
#     if carry != 0:
#         ll.add(carry)
#     return ll
# TC: O(n)
# SC: O(n) - because we create a list for sum that takes o(n) space

list1 = LinkedList()
list2 = LinkedList()
list1.generate(3,1,9)
list2.generate(3,1,9)
print(list1)
print(list2)
print(sum_list(list1, list2))