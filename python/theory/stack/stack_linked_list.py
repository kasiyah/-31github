class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    # TC: O(1) - creating empy list
    # SC: O(1) - haven't inserted any elements into list

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    # TC: O(1) 
    # SC: O(1)
    
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    # TC: O(1) 
    # SC: O(1)

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
    # TC: O(1) 
    # SC: O(1)
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

    def delete(self):
        self.LinkedList.head = None

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
print(customStack.isEmpty())
print("----------------")
print(customStack.pop())
print("----------------")
print(customStack)
print("----------------")
print(customStack.peek())
print("----------------")
customStack.delete()
print(customStack)


# Time and Space Complexity of Stack operations with Linked List
# Operation            | Time Complexity | Space Complexity
# -------------------------------------------------------
# Create Stack         |  O(1)           |   O(1)
# Push                 |  O(1)           |   O(1)
# Pop                  |  O(1)           |   O(1)
# Peek                 |  O(1)           |   O(1)
# isEmpty              |  O(1)           |   O(1)
# Delete Entire Stack  |  O(1)           |   O(1)



# When to use / avoid Stack

# USE:
# - LIFO Functionaity
# - The chance of data corruption is minimum

# AVOID: 
# - Random access is not possible