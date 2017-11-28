# Data Structures

[![Build Status](https://travis-ci.org/allanliebold/data-structures.svg?branch=master)](https://travis-ci.org/allanliebold/data-structures)

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


## Double-Ended Queue (Deque)
A queue that allows data to be added and removed at both ends.

append(data): Adds a new node to the back (tail) of the deque with passed data. Time complexity: O(1)

append_left(data): Adds a new node to the front (head) of the deque with passed data. Time complexity O(1)

pop(): Removes the node at the back of the deque and returns its data. Time complexity O(1)

pop_left(): Removes the node at the front of the deque and returns its data. Time complexity: O(1)

peek(): Returns the value of the node at the back of the deque. Time complexity: O(1)

peek_left(): Returns the value of the node at the front of the deque. Time complexity: O(1)

size(): Returns the length of the deque. Time complexity: O(1)

## Binary Max-Heap
Tree-type data structure that is filled with new values from left to right, and is organized so that parent nodes are greater than child nodes.

push(data): Adds a new value to the end of the tree, and re-sorts based on rule that parent nodes must be greater than child nodes. O(log n)

pop(): Removes value from top of the heap, and re-sorts based on rule that parent nodes must be greater than child nodes. O(log n)

## Priority Queue
A queue with values that has priorities associated with each item. When an item is popped from the queue, the highest priority item is always returned.

insert(data, priority): Inserts value into queue, and accepts an optional argument for the value's priority. Default priority is set to 0. O(1)

pop(): Removes the most important item from the queue and returns its value. O(1)

peek(): Returns the most important item without removing it from the queue. O(1)

## Graph
Structure that includes nodes with connections(edges).

add_node(val): Inserts a new node with the passed value into the graph. O(1)

add_edge(val1, val2): Inserts an edge connecting val1 to val2. O(1)

del_node(val): Removes node containing passed value from the graph. O(1)

del_edge(val1, val2): Removes edge connecting the two values passed. O(1)

has_node(val): Returns True if node containing val is in the graph. Otherwise, returns False. O(1)

neighbors(val): Returns list of all nodes connected to node containing val by edges.

adjacent(val1, val2): Returns True if there is an edge connecting val1 and val2. False if not.

## Graph Traversal
Utilizes graph structure to return path of traversal given a starting value.

dfs(graph, node): Returns list of nodes visited in depth-first order, starting with first node passed as an argument. O(n^2)

bfs(graph, node): Returns list of nodes visited in breadth-first order, starting with first node passed as an argument. O(n)

## Graph With Weighted Edges
Graph with edges that include a value representing distance between nodes.

## Authors: Matt Favoino, Allan Liebold
