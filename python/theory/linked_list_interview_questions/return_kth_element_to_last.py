from linked_list import LinkedList

def nthToLast(ll,n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(n):    #-------------> O(n)
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    
    while pointer2:       #-------------> O(n)
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1
    #TC: O(n)
    #SC: O(1)

customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
print(nthToLast(customLL,10))
print(customLL)