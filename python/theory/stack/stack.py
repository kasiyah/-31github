###############################
# Stack LIFO
###############################
# - data structure that stores items in a Last in/First Out manner
#   - pile of plates, pile of books, etc
# - whenever we need functionality in our app that utilizes the last coming data first
#   - back button in the browser

###############################
# Stack Operations
###############################
# - Create Stack
# - Push
# - Pop
# - Peek 
# - isEmpty
# - isFull
# - deleteStack

##############################################
# Create Stack using List without size limit
##############################################
# Stack Using List
# - Easy to Implement
# - Speed problem when it grows 
#   - items in a list are stored with the goal of providing fast access to the random elements in the list.
#     at a high level, this means that the items are stored next to each other in memory.
#     So if our stack grows bigger than the block of the memory that currently holds in, 
#     the python needs to do some memory allocation. And this is very time consuming operation.

class Stack:
    def __init__(self):
        self.list = []         #-----------> O(1)

    def __str__(self):
        if self.list == None:
            return "Stack does not exist"
        # values = reversed(self.list)
        # values = [str(x) for x in values]
        # return '\n'.join(values)
        return '\n'.join(map(str, self.list[::-1]))
    # TC: O(1)
    # SC: O(1)
    
################################
# isEmpty Method
################################
    def isEMpty(self):
        if self.list == []:
            return True
        else:
            return False
    # TC: O(1)
    # SC: O(1)

################################
# Push Method
################################
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"
    # TC: Amortized Constant 
    #   - Whenever the list needs to allocate more memory,it allocates room for a few items more than it actually needs to avoid  
    #   - having reallocate on each call.So every time when it reaches the memory size, it will reallocate the memory.
    #   - This means that append method in the list has amortized constant. So the allocation overhead may push behavior towards
    #   - O(n) time complexity. Even in the worst cases if we have more elements in the list It might take O(n^2) time complexity.
    # SC: O(1)

################################
# Pop Method
################################
    def pop(self):
        if self.isEMpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
    # TC: O(1)
    # SC: O(1)  


################################
# Peek Method
################################
    def peek(self):
        if self.isEMpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list)-1]
    # TC: O(1)
    # SC: O(1) 

################################
# Delete Stack Method
################################
    def delete(self):
        self.list = None
        return self.list
    # TC: O(1)
    # SC: O(1) 




customStack = Stack()
#print(customStack.isEMpty())
customStack.push(1)
customStack.push(4)
customStack.push(3)
#print(customStack)
# print(customStack.pop())
# print(customStack)
#print(customStack.peek())
print(customStack)
customStack.delete()
print(customStack.isEMpty())
print(customStack)