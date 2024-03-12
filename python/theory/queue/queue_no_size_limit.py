class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        if self.items == None:
            return "The queue does not exist"
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"
        # TC: Amortised TC, depending on the size of the list TC can go up to O(n) or O(n^2)
        # SC: O(1)

    def dequeue(self):
        if self.isEmpty():
            return "There is not any elements in the queue"
        else:
            return self.items.pop(0)
        # TC: O(n) - since when we use pop method all elements should shift one space
        # SC: O(1)

    def peek(self):
        if self.isEmpty():
            return "There is not any elements in the queue"
        else:
            return self.items[0]
        # TC: O(1)
        # SC: O(1)

    def delete(self):
        self.items = None
        # TC: O(1)
        # SC: O(1)

customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
customQueue.delete()
print(customQueue)

# Time and Space Complexity of Queue operations with Python list
# Operation            | Time Complexity | Space Complexity
# -------------------------------------------------------
# Create Queue         |  O(1)           |   O(1)
# Enqueue              |  O(n)/O(n^2)    |   O(1)
# Dequeue              |  O(n)           |   O(1)
# Peek                 |  O(1)           |   O(1)
# isEmpty              |  O(1)           |   O(1)
# Delete Entire Queue  |  O(1)           |   O(1)