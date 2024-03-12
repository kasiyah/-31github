class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
        # TC: O(1)
        # SC: O(1)
        
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
        # TC: O(1)
        # SC: O(1)  

    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None 
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode
        # TC: O(1)
        # SC: O(1)
    
    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head.value
        # TC: O(1)
        # SC: O(1)

    def delete(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            self.linkedList.head = None 
            self.linkedList.tail = None
        # TC: O(1)
        # SC: O(1)

customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.isEmpty())
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
print(customQueue.delete())
print(customQueue)

# Time and Space Complexity of Queue operations using Linked List
# Operation            | Time Complexity | Space Complexity
# -------------------------------------------------------
# Create Queue         |  O(1)           |   O(1)
# Enqueue              |  O(1)           |   O(1)
# Dequeue              |  O(1)           |   O(1)
# Peek                 |  O(1)           |   O(1)
# isEmpty              |  O(1)           |   O(1)
# Delete Entire Queue  |  O(1)           |   O(1)