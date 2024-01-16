# ##############################################################
# Linked List
# ##############################################################
# - is a form of sequential collection and it does not have to be in order
# - made up of independent nodes that may contain any type of data and each node has a reference to the next node in the link
# - head has reference to the first node. Head is needed to know where the linked list starts, to locate the linked list in the memory
# - tail reference to the last node. Need to increase efficiency of the code when inserting at the end of linked list
# - the nodes in linked list are not contiguous
# - node consists of two parts: 
#     - value of node
#     - reference to the next node - physical location of the next node

# ##############################################################
# Linked Lists vs Lists/Arrays
# ##############################################################

# Python list                     |                Linked List
# ------------------------------------------------------------------------
# has indexes                     | no indexes
# elements are contiguous         | elements are located anywhere in memory
#                                 | variable head points to 1st node
#                                 | variable tail points to last node
#                                 | last node points to none


# ##############################################################
# Types of Linked Lists
# ##############################################################
# - Singly Linked List:
#     - each node in the list stores the value and reference to the next node in the linked list 
#       (gives flexibility of adding and removing nodes at run time)
#     - last node always points to null
# - Circular Singly Linked List
#     - the last node of this list stores reference to the first node
#     - Eg:in chess game after last player's turn we need to go to the 1st player
# - Doubly Linked List
#     - two references from each node : reference to previous node and reference to the next node
#     - Eg: in music player to be able to go to next and previous song
# - Circular Doubly Linked List
#     - two references from each node : reference to previous node and reference to the next node
#     - the last node of this list stores reference to the first node
#     - Eg: to look through the list infinitely. Mac cmd+shift+tab function allows to scroll through open apps infinitely until we select the needed app


# ##############################################################
# Linked List in Memory
# ##############################################################
# - node of linked list are not stored contagiously in memory, allocation is random


# ##############################################################
# Node Class
# ##############################################################
# - composed of value and pointer to the next node
# {
#     "value": 10,
#     "next": None
# }

# When we create a linked list class, we use node class inside linked list and 
# it's going to maintain the structure of linked list itself.

# class Node:
#     # create a constructor that will have attributes of the node class
#     def __init__(self, value):  #------------------------------> O(1)
#         self.value = value  #----------------------------------> O(1)
#         self.next = None   #-----------------------------------> O(1)
 
# new_node = Node(10)  #-----------------------------------------> O(1)
# print(new_node)


# ##############################################################
# Linked List Class
# ##############################################################
# # creating empty Linked List
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
 
# # creating linked list consisting of one node
# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node


# ##############################################################
# class Node:
#     def __init__(self, value): 
#         self.value = value  
#         self.next = None
 
# # creating linked list consisting of one node
# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)  #---------------------> o(1)
#         self.head = new_node    #---------------------> o(1)
#         self.tail = new_node    #---------------------> o(1)
#         self.length = 1         #---------------------> o(1)
 
# new_linked_list = LinkedList(10)
# # print value of linked list node
# print(new_linked_list.head.value)

# Time Complexity: 0(1)
# Space Complexity: O(1)


# ##############################################################
# Insertion to Linked List in Memory
# ##############################################################
# 1. At the beginning of the linked list
#     - allocate a random memory in the heap for new node
#     - point new node to the 1st node in linked list
#     - point head to the new node

# 2. After a node in the middle of linked list
#     - traverse from head to find a node after which we want to insert a new node
#     - allocate a random memory in the heap for new node
#     - point current node to the new node
#     - point new node to the next node in linked list

# 3. At the end of the linked list
#     - traverse from head to find the last node
#     - allocate a random memory in the heap for new node
#     - point last node to the new node
#     - point tail to new node

# Time and Space Complexity of Singly Linked List
Operation         | Time Complexity | Space Complexity
-------------------------------------------------------
Create            |  O(1)           |   O(1)
Append            |  O(1)           |   O(1)
Prepend           |  O(1)           |   O(1)
Insert            |  O(n)           |   O(1)
Search            |  O(n)           |   O(1)
traverse          |  O(n)           |   O(1)
Get               |  O(n)           |   O(1)
Set               |  O(n)           |   O(1)
Pop First         |  O(1)           |   O(1)
Pop               |  O(n)           |   O(1)
Remove            |  O(n)           |   O(1)
Delete all Nodes  |  O(1)           |   O(1)
