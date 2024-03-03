###############################
# Queue FIFO
###############################
# - data structure that stores items in a First in/First Out manner
#   - a new addition to the queue happens at the end of the queue
#   - First person in the queue will be served first
# - whenever we need functionality in our app that utilizes the first coming data first, while others wait for their turn
#   - point sale system in the restaurant
#   - single shared printer
#   - call center application

###############################
# Queue Operations
###############################
# - Create Queue
# - Enqueue
# - Dequeue
# - Peek 
# - isEmpty
# - isFull
# - delete Queue

###############################
# Queue Implementation
###############################
# 1. Python List
#    - Queue without capacity
#      - if we set maximum size, the queue becomes time efficient.
#         Otherwise, lists are quite so slow for this purpose. 
#         Because inserting and deleting an element at the beginning 
#         requires shifting all elements one step left. So this takes O(n) time compexity.
#    - Queue with capacity(Circular Queue)
# 2. Linked list