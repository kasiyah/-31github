#################################
# Circular Doubly Linked List
#################################
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.tail = None

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
# Append Method CDLL
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
                
    

circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
print([node.value for node in circularDLL])


