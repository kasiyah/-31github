from linked_list import LinkedList

def remove_duplicates(ll):
    if ll.head is None:
        return
    seen = set()
    curNode = ll.head
    seen.add(curNode.value)
    while curNode.next:
        if curNode.next.value in seen:
            print(curNode.next.value)
            curNode.next = curNode.next.next
        else:
            seen.add(curNode.next.value)
            curNode = curNode.next
    ll.tail = curNode
    print(seen)
    #return ll.head

customLL = LinkedList()
customLL.generate(20,0,99)
print(customLL)
remove_duplicates(customLL)
print(customLL)

# Solution
"""
def remove_duplicates(ll):
    if ll.head is None:
        return
 
    current_node = ll.head
    prev_node = None
 
    while current_node:
        runner = current_node
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        prev_node = current_node
        current_node = current_node.next
 
    ll.tail = prev_node  
    return ll.head

Explanation:

def remove_duplicates(ll): 
    - This is the function definition for remove_duplicates. It takes one argument ll which is a LinkedList object.
if ll.head is None: 
    - This is a condition to check if the head of the LinkedList ll is None. If it's None, 
    it means the list is empty and there are no duplicates to remove.

    - return - If the LinkedList ll is empty (i.e., the head is None), the function ends and returns None.

current_node = ll.head 
    - This line sets current_node to the head of the LinkedList. current_node will be used to traverse the list.

prev_node = None 
    - This line initializes prev_node as None. prev_node will be used to keep track of the node before current_node.

while current_node: 
    - This is the start of a while loop that runs as long as current_node is not None. 
    This loop is used to traverse the list.

runner = current_node 
    - Inside the while loop, runner is set to the current_node. 
    runner will be used to look ahead in the list for duplicates.

while runner.next: 
    - This is a nested while loop that runs as long as runner.next is not None. 
    This loop is used to check for duplicates of current_node's value in the remaining list.

if runner.next.value == current_node.value: 
    - This is a condition to check if the next value in the list (after runner) is the same as the value of current_node.

runner.next = runner.next.next 
    - If the above condition is true, it means we have found a duplicate. So, we bypass the duplicate node 
    by changing runner.next to runner.next.next.

else: runner = runner.next 
    - If the above condition is false, we move runner one step forward in the list.

prev_node = current_node 
    - After we have checked all the remaining list for duplicates of current_node, we set prev_node to current_node.

current_node = current_node.next 
    - We move current_node one step forward in the list.

ll.tail = prev_node 
    - After the outer while loop ends (meaning we have traversed the entire list), prev_node is the last node in the list. 
    We set ll.tail to prev_node, effectively updating the tail of the LinkedList.

return ll.head 
    - The function ends by returning the head of the LinkedList. This is not strictly necessary as the LinkedList 
    is modified in-place, but it could be useful if you want to chain operations.

    
This function works by checking each node in the LinkedList against all the subsequent nodes for duplicates. 
If a duplicate is found, it's removed by updating the next attribute of the node before it, thus bypassing the duplicate node. 
In the end, the tail of the LinkedList is updated to the last node in the list.

The time and space complexity for this function can be explained as follows:
- def remove_duplicates(ll): - Defining a function doesn't affect the time or space complexity.
- if ll.head is None: - Checking a condition takes a constant amount of time, so it contributes O(1) to the time complexity.
- return - Returning from a function takes a constant amount of time, so it contributes O(1) to the time complexity.
- current_node = ll.head - Setting a variable to a value takes a constant amount of time and space, so it contributes O(1) 
to both time and space complexity.
- prev_node = None - Setting a variable to a value takes a constant amount of time and space, so it contributes O(1) 
to both time and space complexity.
- while current_node: - This is the start of a loop that runs for N iterations, where N is the number of nodes in the LinkedList.
- runner = current_node - Setting a variable to a value takes a constant amount of time and space, so it contributes O(1) 
to both time and space complexity. However, since this is inside the while loop, it actually contributes O(N) to the time 
complexity when considering the entire operation of the loop.
- while runner.next: - This is the start of a nested loop. For each node in the LinkedList, it runs for N iterations (worst case), 
where N is the number of nodes remaining in the list after the current node.
- if runner.next.value == current_node.value: - Checking a condition takes a constant amount of time, so it contributes O(1) 
to the time complexity. But since this is inside the nested while loop, it actually contributes O(N^2) to the time complexity 
when considering the entire operation of the loop.
- runner.next = runner.next.next - Updating the value of a variable takes a constant amount of time, so it contributes O(1) 
to the time complexity. But since this is inside the nested while loop, it actually contributes O(N^2) to the time complexity 
when considering the entire operation of the loop.
- else: runner = runner.next - Updating the value of a variable takes a constant amount of time, so it contributes O(1) 
to the time complexity. But since this is inside the nested while loop, it actually contributes O(N^2) to the time complexity 
when considering the entire operation of the loop.
- prev_node = current_node - Setting a variable to a value takes a constant amount of time and space, so it contributes O(1) 
to both time and space complexity. However, since this is inside the while loop, it actually contributes O(N) to the time 
complexity when considering the entire operation of the loop.
- current_node = current_node.next - Updating the value of a variable takes a constant amount of time, so it contributes O(1) 
to the time complexity. But since this is inside the while loop, it actually contributes O(N) to the time complexity when
 considering the entire operation of the loop.
- ll.tail = prev_node - Setting a variable to a value takes a constant amount of time and space, so it contributes O(1) 
to both time and space complexity.
- return ll.head - Returning a value from a function takes a constant amount of time, so it contributes O(1) to the time complexity.

Overall Time Complexity: 
    -Since the function has a nested loop that, in the worst case, runs for N^2 iterations, 
    the overall time complexity is O(N^2), where N is the number of nodes in the LinkedList.
Overall Space Complexity: 
    - The function uses a few variables to keep track of the current and previous nodes, but it doesn't use any 
    additional data structures that grow with the size of the input, so the overall space complexity is O(1).
"""

