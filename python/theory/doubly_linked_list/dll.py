# #############################################
# Doubly Linked List 
# #############################################
# - is similars the single linked list
#     - each node has pointer no next and prev nodes
#       - last node next points to None
#       - first node prev points to None
#       - this allows to come from first node to last node 
#         and from last node to first node unlik sinly linked list 

# #############################################
# Creating DLL
# #############################################
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    # TC: O(1)
    # SC: O(1)
    
    def __str__(self):
        return str(self.value)
        #return f"{self.prev} <- {self.value} -> {self.next}"
    # TC: O(1)

class DoublyLinkeList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

# #############################################
# __str__ Method DLL
# #############################################

    def __str__(self):
        temp_node = self.head 
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' <-> '
            temp_node = temp_node.next
        return result
    # TC: O(n)
    # SC: O(1)

# #############################################
# Append Method
# #############################################
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
    # TC: O(1)
    # SC: O(1)   

# #############################################
# Prepend Method
# #############################################
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    # TC: O(1)
    # SC: O(1) 
        
# #############################################
# Traversal Method
# #############################################
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next
    # TC: O(n)
    # SC: O(1)
            
# #############################################
# Reverse Traversal Method
# #############################################
    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node)
            current_node = current_node.prev
    # TC: O(n)
    # SC: O(1)

# #############################################
# Search Method
# #############################################
    def search(self, target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return -1
    # TC: O(n)
    # SC: O(1)

# #############################################
# Get Method
# #############################################
# imporoved version of get method
# if index is in first half we start from head
# is index is in second half we start from tail
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        # we are looking at floor number
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            # we traverse from last node until the index and we decrease index by 1 ---> -1
            for _ in range(self.length -1, index, -1):
                current_node = current_node.prev
        return current_node   
    # TC: O(n) - even through we traverse only half of the loop, we should drop the constant
    # SC: O(1)

# #############################################
# Set Method
# #############################################
    def set(self, index, value):
        node = self.get(index)   #--------------------> O(n)
        if node:
            node.value = value
            return True
        return False   
    # TC: O(n) - since get method takes O(n)
    # SC: O(1)

# #############################################
# Insert Method
# #############################################
    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Index out of bounds.")
            return
        new_node = Node(value)
        if index == 0:
            # new_node.next = self.head
            # self.head.prev = new_node
            # self.head = new_node
            self.prepend(value)            #--------------------> O(1)
            return
        elif index == self.length:
            # self.tail.next = new_node
            # new_node.prev = self.tail
            # self.tail = new_node
            self.append(value)              #--------------------> O(1)
            return
        else:
            temp_node = self.get(index-1)   #--------------------> O(n)
            new_node.next = temp_node.next
            new_node.prev = temp_node
            temp_node.next.prev = new_node
            temp_node.next = new_node
        self.length += 1  
    # TC: O(n) - since get method takes O(n)
    # SC: O(1)
        
# #############################################
# Pop First Method
# #############################################
    def pop_first(self):
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node  
    # TC: O(1)
    # SC: O(1)

# #############################################
# Pop Method
# #############################################
    def pop(self):
        if not self.head:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node  
    # TC: O(1)
    # SC: O(1)

# #############################################
# Remove Method
# #############################################
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        if not self.head:
            return None
        popped_node = self.get(index)   #--------------------> O(n)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1
        return popped_node  
    # TC: O(n)
    # SC: O(1)

# new_node = Node(10)
# print(new_node)
doublyLinkedList = DoublyLinkeList()
print(doublyLinkedList)
doublyLinkedList.append(20)
doublyLinkedList.append(30)
doublyLinkedList.prepend(10)
# doublyLinkedList.traverse()
# doublyLinkedList.reverse_traverse()
# print(doublyLinkedList)
# print(doublyLinkedList.search(200))
# print(doublyLinkedList.get(-1))
# print(doublyLinkedList)
# print(doublyLinkedList.set(1,40))
# print(doublyLinkedList)
# print(doublyLinkedList.insert(3,20))
# print(doublyLinkedList)
# print(doublyLinkedList.pop_first())
# print(doublyLinkedList)
# print(doublyLinkedList.pop())
print(doublyLinkedList)
print(doublyLinkedList.remove(1))
print(doublyLinkedList)


# # Time and Space Complexity of Doubly Linked List
# Operation         | Time Complexity | Space Complexity
# -------------------------------------------------------
# Create            |  O(1)           |   O(1)
# Append            |  O(1)           |   O(1)
# Prepend           |  O(1)           |   O(1)
# Insert            |  O(n)           |   O(1)
# Search            |  O(n)           |   O(1)
# traverse          |  O(n)           |   O(1)
# Get               |  O(n)           |   O(1)
# Set               |  O(n)           |   O(1)
# Pop First         |  O(1)           |   O(1)
# Pop               |  O(1)           |   O(1)
# Remove            |  O(n)           |   O(1)
# Delete all Nodes  |  O(1)           |   O(1)
