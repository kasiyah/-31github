class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        if self.list == None:
            return "Stack does not exist"
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else: 
            return False
        # TC: O(1)
        # SC: O(1)

    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has een successfully inserted"
        # TC: Amortised TC, depending on the size of the list TC can go up to O(n)
        # SC: O(1)


    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[len(self.list) - 1]
        # TC: O(1)
        # SC: O(1)
    
    def delete(self):
        self.list = None
             
customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
customStack.pop()
print(customStack)
print(customStack.peek())
customStack.delete()
print(customStack)

# Time and Space Complexity of Stack operations with list
# Operation            | Time Complexity | Space Complexity
# -------------------------------------------------------
# Create Stack         |  O(1)           |   O(1)
# Push                 |  O(1)/O(n^2)    |   O(1)
# Pop                  |  O(1)           |   O(1)
# Peek                 |  O(1)           |   O(1)
# isEmpty              |  O(1)           |   O(1)
# Delete Entire Stack  |  O(1)           |   O(1)




        
        