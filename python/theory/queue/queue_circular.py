class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
        # TC: O(1)
        # SC: O(n) - if the maxSize is n, the SC is O(n)

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else: 
            return False
        # TC: O(1)
        # SC: O(1)

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        # TC: O(1)
        # SC: O(1)

    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of queue"
        # TC: O(1)
        # SC: O(1)

    def dequeue(self):
        if self.isEmpty():
            return "There is not any elements in the queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
        # TC: O(1)
        # SC: O(1)

    def peek(self):
        if self.isEmpty():
            return "There is not any elements in the queue"
        else:
            return self.items[self.start]
        # TC: O(1)
        # SC: O(1)

    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1
        # TC: O(1)
        # SC: O(1)


customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.isFull())
print(customQueue.isEmpty())
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
customQueue.delete()
print(customQueue)

# Time and Space Complexity of Circular Queue operations with Python list
# Operation            | Time Complexity | Space Complexity
# -------------------------------------------------------
# Create Queue         |  O(1)           |   O(n)
# Enqueue              |  O(1)           |   O(1)
# Dequeue              |  O(1)           |   O(1)
# Peek                 |  O(1)           |   O(1)
# isEmpty              |  O(1)           |   O(1)
# isFull               |  O(1)           |   O(1)
# Delete Entire Queue  |  O(1)           |   O(1)
    