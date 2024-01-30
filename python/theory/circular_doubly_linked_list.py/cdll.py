#################################
# Circular Doubly Linked List
#################################
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
#####################################
# Create CDLL
#####################################
    def createCDLL(self, nodeValue):
        new_node = Node(nodeValue)   #--------------------------> O(1)
        self.head = new_node         #--------------------------> O(1)
        self.tail = new_node         #--------------------------> O(1)
        new_node.next = new_node     #--------------------------> O(1)
        new_node.prev = new_node     #--------------------------> O(1)
        self.length += 1             #--------------------------> O(1)
        return "The CDLL is created successfully"
    # TC: O(1)
    # SC: O(1)

#####################################
# Insert Method CDLL
#####################################
    def insertCDLL(self, value, location):
        if not self.head:
            return "The CDLL does not exist"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:     #---------------> O(n)
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node
            self.length += 1
            return "The node has been successfully inserted"
        # TC: O(n)
        # SC: O(1)
                
#####################################
# Traverse Method CDLL
#####################################
    def traverseCDLL(self):  
        if self.head is None:
            print("There is not any nodes for traversal")
        else:
            temp_node = self.head
            while temp_node:                    #---------------> O(n)
                print(temp_node.value)
                if temp_node == self.tail:
                    break
                temp_node = temp_node.next 
        # TC: O(n)
        # SC: O(1)

#####################################
# Reverse Traverse Method CDLL
#####################################
    def reverseTraverseCDLL(self):  
        if self.head is None:
            print("There is not any nodes for reverse traversal")
        else:
            temp_node = self.tail
            while temp_node:                    #---------------> O(n)
                print(temp_node.value)
                if temp_node == self.head:
                    break
                temp_node = temp_node.prev 
        # TC: O(n)
        # SC: O(1)

#####################################
# Search Method CDLL
#####################################
    def searchCDLL(self, value):  
        if self.head is None:
            print("There is not any nodes in CDLL")
        else:
            temp_node = self.tail
            while temp_node:                    #---------------> O(n)
                if temp_node.value == value:
                    return temp_node.value
                if temp_node == self.head:
                    return "The value does not exist in CDLL"
                temp_node = temp_node.prev 
        # TC: O(n)
        # SC: O(1)

#####################################
# Delete Node Method CDLL
#####################################
    def deleteNode(self,location):  
        if self.head is None:
            return "There is not any node to delete"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                temp_node = self.head
                index = 0
                while index < location-1:         #-------------------> O(n)
                    temp_node = temp_node.next
                    index += 1
                temp_node.next = temp_node.next.next
                temp_node.next.prev = temp_node
            print("The node has been successfully deleted.") 
        # TC: O(n)
        # SC: O(1)
            
#####################################
# Delete All Nodes Method CDLL
#####################################
    def delete_all(self):
        if self.head is None:
            print("There is not any nodes to delete")
        else:
            self.tail.next = None
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None
            print("CDLL was deleted successfully.")

            
circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
# print([node.value for node in circularDLL])
# circularDLL.traverseCDLL()
# circularDLL.reverseTraverseCDLL()
# print(circularDLL.searchCDLL(2))
# print([node.value for node in circularDLL])
# circularDLL.deleteNode(3)
print([node.value for node in circularDLL])
circularDLL.delete_all()
print([node.value for node in circularDLL])


# Time and Space Complexity of Circular Doubly Linked List
# Operation         | Time Complexity | Space Complexity
# -------------------------------------------------------
# Create            |  O(1)           |   O(1)
# Insert            |  O(n)           |   O(1)
# Search            |  O(n)           |   O(1)
# Traverse(-> | <-) |  O(n)           |   O(1)
# Delete one Node   |  O(n)           |   O(1)
# Delete all Nodes  |  O(n)           |   O(1)