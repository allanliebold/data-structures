# Data Structures

## Singly-Linked List
A data structure that links together nodes in one direction, beginning at a head 
node.

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
Last in first out. 

push(data)
Time complexity: O(1)

pop()
Time complexity: O(1)

## Doubly-Linked List
Similar to a Singly-Linked list, but each node also points to the previous node. 
In addition to the head, the list also contains a tail node. 

push(data)
Time complexity: O(1)

pop()
Time complexity: O(1)

append(data)
Time complexity: O(1)

shift()
Time complexity: O(1)

remove(data)
Time complexity: O(n)