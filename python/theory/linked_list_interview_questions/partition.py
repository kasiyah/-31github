from linked_list import LinkedList

def partition(ll,x):
    curNode = ll.head
    ll.tail = ll.head

    while curNode:          #-------------------> O(n)
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x:
            curNode.next = ll.head
            ll.head = curNode
        else: 
            ll.tail.next = curNode
            ll.tail = curNode
        curNode = nextNode

    if ll.tail.next is not None:
        ll.tail = None
    #TC: O(n)
    #SC: O(1)

customLL = LinkedList()
customLL.generate(20,0,99)
print(customLL)
partition(customLL,50)
print(customLL)