# #############################################
# Circular Single Linked List 
# #############################################
# - is exactly same as the single linked list.
#     - in the single linked list the last node points to the none.
#     - in circular single linked list it points to the first node.

# #############################################
# Creating CSL
# #############################################
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    # epmty CSLL
    def __init__(self):
        self.head = None    
        self.tail = None
        self.length = 0
    # Time Complexity: O(1) - we just create head and tail that point to none, length equals to 0
    # Space Complexity: O(1) - it is not allocating any memory in this case

    # one node
    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
    # Time Complexity: O(1) - we just create head and tail that point to none, length equals to 0
    # Space Complexity: O(1) - we are inserting only one node ---> constant SC

# #############################################
# Append MEthod CSL
# #############################################
    def append(self, value):
        new_node = Node(value)      
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length +=1
        # Time Complexity: O(1) - inserting only one node
        # Space Complexity: O(1) - we are inserting only one node ---> constant SC


csLinkedList = CSLinkedList()
csLinkedList.append(10)
csLinkedList.append(20)
print(csLinkedList.head.value)
print(csLinkedList.head.next.value)