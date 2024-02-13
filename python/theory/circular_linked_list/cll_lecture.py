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
            raise Exception ("Index out of bound")
        if index == 0:
            if self.length == 0:
                self.head = self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

        return new_node
#############################################
# Traversal in CSLL
#############################################
    def traverse(self):
        temp_node = self.head 
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break

#############################################
# Search CSLL
#############################################
    def search(self,target):
        temp_node = self.head 
        while temp_node is not None:
            if temp_node.value == target:
                return True
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return False

#############################################
# Get Method CSLL
#############################################
    def get(self,index):
        temp_node = self.head 
        if index < 0 or index >= self.length:
            return None
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node


#############################################
# Set Method CSLL
#############################################
    def set(self,index,value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False




csLinkedList = CSLinkedList()
csLinkedList.append(10)
csLinkedList.append(20)
csLinkedList.append(50)
csLinkedList.append(70)
csLinkedList.append(90)
csLinkedList.append(60)
csLinkedList.append(30)
print(csLinkedList)
print(csLinkedList.insert(0,65))
print(csLinkedList)
