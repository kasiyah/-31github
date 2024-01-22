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
    
    # str method for Node
    def __str__(self):
        return str(self.value)

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
#############################################
# Printing CSLL
#############################################
    def __str__(self):
        temp_node = self.head 
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result


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


#############################################
# Prepend MEthod SLL
#############################################
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else: 
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
        # Time Complexity: O(1) - inserting only one node
        # Space Complexity: O(1) - we are inserting only one node ---> constant SC
    

#############################################
# Insert Method CSLL
#############################################
    def insert(self,index, value):
        new_node = Node(value)
        temp_node = self.head
        if index > self.length or index < 0:
            raise Exception("Index out of range")
        if index == 0:
            # self.prepend(value)
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            # self.append(value)
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            for _ in range(index-1):    #--------O(n)
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node  
        self.length += 1
    # Time Complexity: O(n) - since we loop through list till we find needed index
    # Space Complexity: O(1) - we are inserting only one node ---> constant SC

#############################################
# Traversal in CSLL
#############################################
    def traverse(self):
        current = self.head
        # edge case when list is empty is covered here, since it checks that current is not None
        while current is not None: 
            print(current.value)
            current = current.next
            if current == self.head:
                break
    # Time Complexity: O(n) - since we loop through list
    # Space Complexity: O(1) - we are inserting only one node ---> constant SC

#############################################
# Search CSLL
#############################################
    def search(self,target):
        current = self.head
        # edge case when list is empty is covered here, since it checks that current is not None
        while current is not None: 
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False
    # Time Complexity: O(n) - since we loop through list until we find target
    # Space Complexity: O(1) - we are inserting only one node ---> constant SC

#############################################
# Get Method CSLL
#############################################
    def get(self,index):
        current = self.head
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        for _ in range(index): 
            current = current.next
        return current
    # Time Complexity: O(n) - since we loop through list until we find index
    # Space Complexity: O(1) - we are inserting only one node ---> constant SC


#############################################
# Set Method CSLL
#############################################
    def set(self,index,value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False
    # Time Complexity: O(n) - since we loop through list until we find index where to set value
    # Space Complexity: O(1) - we are inserting only one node ---> constant SC

#############################################
# Pop First Method CSLL
#############################################
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
    # Time Complexity: O(1)  
    # Space Complexity: O(1) 

#############################################
# Pop Method CSLL
#############################################
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
        self.length -= 1
        return popped_node
    # Time Complexity: O(n) - since we loop through list untill we find node prev to tail  
    # Space Complexity: O(1) 


#############################################
# Remove Method CSLL
#############################################
    def remove(self, index):
        if index <0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()      #-------O(1)
        elif index == self.length-1:
            return self.pop()            #-------O(n)
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    # Time Complexity: O(n) - since we use pop method 
    # Space Complexity: O(1) 

#############################################
# Traversal in CSLL
#############################################
    def delete_all(self):
        if self.length == 0:
            return None
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0 
    # Time Complexity: O(1)
    # Space Complexity: O(1)



csLinkedList = CSLinkedList()
csLinkedList.append(10)
csLinkedList.append(20)
print(csLinkedList.head.value)
print(csLinkedList.head.next.value)
print(csLinkedList)
csLinkedList.prepend(40)
print(csLinkedList)
csLinkedList.insert(1,60)
# print(csLinkedList)
# print(csLinkedList.tail.value)
# csLinkedList.traverse()
# print(csLinkedList.search(50))
# print(csLinkedList.search(10))
# print(csLinkedList.get(0))
# print(csLinkedList)
# print(csLinkedList.set(1,30))
# print(csLinkedList)
# print(csLinkedList.pop_first())
# print(csLinkedList)
# print(csLinkedList.pop())
# print(csLinkedList)
# print(csLinkedList.remove(0))
print(csLinkedList)
csLinkedList.delete_all()
print(csLinkedList)
csLinkedList.delete_all()


# # Time and Space Complexity of Circular Singly Linked List
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
# Pop               |  O(n)           |   O(1)
# Remove            |  O(n)           |   O(1)
# Delete all Nodes  |  O(1)           |   O(1)
