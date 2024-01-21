############################################
# Linked List Methods 
############################################
class Node:
    def __init__(self, value): 
        self.value = value  
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # overriding str method for printing linked list      
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
               result += ' -> ' 
            temp_node = temp_node.next
        return result
    
    # append method
    def append(self, value):
        new_node = Node(value)         #----------------------------O(1)    
        if self.head is None:          #----------------------------O(1)
            self.head = new_node       #----------------------------O(1)
            self.tail = new_node       #----------------------------O(1)
        else: 
            self.tail.next = new_node  #----------------------------O(1)
            self.tail = new_node       #----------------------------O(1)
        self.length += 1               #----------------------------O(1)
        # Time Complexity: O(1) - Since each operation is taking constant time and do not depend on the size of the input list
        # Space Complexity: O(1) - only a single node is created during this operation regardless 
        # of the size of the linked list since additional space is not required
               

    # prepend method
    def prepend(self, value):
        new_node = Node(value)            #----------------------------O(1)       
        if self.head is None:             #----------------------------O(1)    
            self.head = new_node          #----------------------------O(1)     
            self.tail = new_node          #----------------------------O(1)  
        else: 
            new_node .next = self.head    #----------------------------O(1)  
            self.head = new_node          #----------------------------O(1)    
        self.length += 1                  #----------------------------O(1) 
        # Time Complexity: O(1) - Since each operation is taking constant time and do not depend on the size of the input list
        # Space Complexity: O(1) - only a single node is created during this operation regardless 
        # of the size of the linked list since additional space is not required
    
    # insert method
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:         
            self.head = new_node       
            self.tail = new_node    
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):     #----------------- O(n)
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1
        return True
        # Time Complexity: O(n) - Since for looopp is used to search for index
        # Space Complexity: O(1) - only a single node is created during this operation regardless 
        # of the size of the linked list since additional space is not required

    # Traversal method of Singly Linked List
    def traverse(self):
        current = self.head          #----------------- O(1) 
        # same as while current is not None:
        while current:               #----------------- O(n) 
            print(current.value)     #----------------- O(1) 
            current = current.next   #----------------- O(1) 
        # Time Complexity: O(n)
        # Space Complexity: O(1) 

    # Search Method in Singly Linked List
    def search(self, target):
        current = self.head               #----------------- O(1) 
        index = 0                         #----------------- O(1) 
        # same as while current is not None:
        while current:                    #----------------- O(n) 
            if current.value == target:   #----------------- O(1) 
                return index              #----------------- O(1) 
            current = current.next        #----------------- O(1) 
            index += 1                    #----------------- O(1) 
        return -1                         #----------------- O(1) 
        # Time Complexity: O(n)
        # Space Complexity: O(1)
    
    # Get Method
    def get(self, index):
        if index == -1:                         #----------------- O(1) 
            return self.tail                    #----------------- O(1) 
        if index < 0 or index >= self.length:   #----------------- O(1) 
            return None                         #----------------- O(1) 
        current = self.head                     #----------------- O(1) 
        # same as while current is not None:
        for _ in range(index):                  #----------------- O(n) 
            current = current.next              #----------------- O(1) 
        return current                          #----------------- O(1) 
        # Time Complexity: O(n)
        # Space Complexity: O(1)

    # Set Method
    def set_value(self, index, value):
        temp = self.get(index)       #----------------- O(n) 
        if temp:                     #----------------- O(1) 
            temp.value = value       #----------------- O(1) 
            return True              #----------------- O(1) 
        return False                 #----------------- O(1) 
        # Time Complexity: O(n)
        # Space Complexity: O(1)

    # Pop First Method
    def pop_first(self):
        if self.length == 0:             #----------------- O(1) 
            return None                  #----------------- O(1) 
        popped_node = self.head          #----------------- O(1) 
        if self.length == 1:             #----------------- O(1)
            self.head = None             #----------------- O(1)
            self.tail = None             #----------------- O(1)
        else:
            self.head = self.head.next   #----------------- O(1) 
            popped_node.next = Node      #----------------- O(1) 
        self.length -= 1                 #----------------- O(1) 
        return popped_node               #----------------- O(1) 
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    
    # Pop Method
    def pop(self):
        if self.length == 0:                     #----------------- O(1) 
            return None                          #----------------- O(1) 
        popped_node = self.tail                  #----------------- O(1) 
        if self.length == 1:                     #----------------- O(1)
            self.head = self.tail = None         #----------------- O(1)
        else:
            temp = self.head                     #----------------- O(1) 
            while temp.next is not self.tail:    #----------------- O(n)
                temp = temp.next                 #----------------- O(1)
            self.tail = temp                     #----------------- O(1)
            temp.next = None                     #----------------- O(1)
        self.length -= 1                         #----------------- O(1) 
        return popped_node                       #----------------- O(1) 
        # Time Complexity: O(n)
        # Space Complexity: O(1)

    # Remove Method
    def remove(self, index):
        if index < -1 or index >= self.length:
            return None                             #----------------- O(1)
        if index == 0:
            return self.pop_first()                 #----------------- O(1)
        if index == self.length-1 or index == -1:
            return self.pop()                       #----------------- O(n)
        prev_node = self.get(index-1)               #----------------- O(n) 
        popped_node = self.get(index)               #----------------- O(1)
        prev_node.next = popped_node.next           #----------------- O(1)
        popped_node.next = None                     #----------------- O(1) 
        self.length -= 1                            #----------------- O(1)
        return popped_node                          #----------------- O(1) 
        # Time Complexity: O(n)
        # Space Complexity: O(1)
    

    # Delete all nodes Method
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0 
        # Time Complexity: O(1)
        # Space Complexity: O(1)

new_linked_list = LinkedList()
new_linked_list.insert(0,50)
print(new_linked_list)
new_linked_list.prepend(10)
new_linked_list.prepend(20)
new_linked_list.prepend(40)
new_linked_list.insert(-1,30)
print(new_linked_list)
new_linked_list.traverse()
print(new_linked_list.search(30))
print(new_linked_list.get(-1))
print(new_linked_list.set_value(2,30))
print(new_linked_list)
print(new_linked_list.pop_first())
print(new_linked_list)
print(new_linked_list.pop())
print(new_linked_list)
print(new_linked_list.remove(-1))
print(new_linked_list.tail.value)
print(new_linked_list.delete_all())
print(new_linked_list)