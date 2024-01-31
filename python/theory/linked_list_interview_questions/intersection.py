from linked_list import LinkedList, Node

def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB 
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):      
        longerNode = longerNode.next

    # will loop until lits are intersecting
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    
    return longerNode
# TC: O(A + B) - where A is length of llA and B is length of llB. TC of len function is O(n)
# SC: O(1)

# helper addition method
def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode

list1 = LinkedList()
list1.generate(3,0,10)

list2 = LinkedList()
list2.generate(5,0,10)

addSameNode(list1,list2,11)
addSameNode(list1,list2,9)

print(list1)
print(list2)

print(intersection(list1, list2))