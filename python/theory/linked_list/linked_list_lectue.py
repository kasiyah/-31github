############################################
# Linked List Methods 
############################################
class Node:
    def __init__(self, value): 
        self.value = value  
        self.next = None

    def __str__(self):
        return str(self.value)

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
    
    # Get Method
    def get(self, index):
        if index == -1:
            return self.tail
        if index < 0 or index >= self.length:
            return "The index is out of bound!"
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    # Set Method
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # Pop First Method
    def pop_first(self):
        if self.head == None:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    # Pop Method
    def pop(self):
        if self.head == None:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head 
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node

    # Remove Method
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1 or index == -1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = self.get(index)
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    # Delete all nodes Method
    def delete_all(self):
        self.head = None
        self.tail = None
        return None
   
new_linked_list = LinkedList()
new_linked_list.prepend(10)
new_linked_list.prepend(20)
new_linked_list.prepend(40)
new_linked_list.prepend(30)
new_linked_list.prepend(60)
new_linked_list.prepend(50)
print()
print(new_linked_list)
print(new_linked_list.get(7))
print(new_linked_list.set_value(2,70))
print(new_linked_list)
print(new_linked_list.pop_first())
print(new_linked_list)
print(new_linked_list.pop())
print(new_linked_list)
print(new_linked_list.remove(2))
print(new_linked_list)
print(new_linked_list.delete_all())
print(new_linked_list)