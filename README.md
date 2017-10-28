# Data Structures

## Singly-Linked List
A data structure that links together nodes in one direction, beginning at a head node. This structure is used for keeping
track of sequentially related data where each piece of data only needs to point to the next in the chain and not back to the
previous one. 

push(data): Adds a new node to the head of the list.
Time complexity: O(1)

pop(): Removes node from the head of the list and returns its value. 
Time complexity: O(1)

size(): Returns the length of the list. 
Time complexity: O(1)

search(data): Iterates over the list to find the node containing the data passed as the
argument. Returns the node, if found, otherwise raises a ValueError.
Time complexity: O(n)

remove(data): Iterates over the list to find the node containing the data passed as the
argument. Reassigns the next attribute of the previous node to the next, to remove the reference to the specified node. Returns the value of the removed node. 
Time complexity: O(n)

display(data): Iterates over the entire list and concatenates a string with each node's value, then prints the complete string. 
Time complexity: O(n)

len(list): Overwrites built in len() function to show the same result as the size() function.
Time complexity: O(1)

print(list): Overwrites built in print() and str() functions to show the same result as the
display() function.
Time complexity: O(n)

## Stack
Data structure where nodes are added and removed from the top of the stack. Last in, first out.

push(data): Adds a new node to the top of the stack with the value passed in as an argument.
Time complexity: O(1)

pop(): Removes the top node from the stack, and returns the value of the node.
Time complexity: O(1)


## Doubly-Linked List
Similar to a Singly-Linked list, but each node also points to the previous node. In addition to the head, the list also
contains a tail node. This is more flexible than a Singly-Linked List, but requires more space in memory. An example of a use 
case is a browser history allowing a user to go backward and forward through visited pages. 

push(data): Adds a new node to the head of the list with the data passed in as an argument.
Time complexity: O(1)

pop(): Removes node at the head of the list, and returns it.
Time complexity: O(1)

append(data): Adds a new node to the tail of the list with the data passed in as an argument.
Time complexity: O(1)

shift(): Removes node at the tail of the list, and returns it.
Time complexity: O(1)

remove(data): Iterates through list, starting from the head, until node with data passed as argument is found. Removes references to the node, and returns the node. If no node contains the data, raises Value Error.
Time complexity: O(n)



## Queue
A data structure where the first node added will be the first removed. 

enqueue(data): Adds a new node to the queue. It will be behind any nodes already enqueued for order to be dequeued. Time complexity: O(1)

dequeue(data): Removes the next node to be dequeued, which should be whatever node remaining in the queue was added first. Time complexity: O(1)

peek(): Returns the value of the next node to be dequeued without removing it. Time complexity: O(1)