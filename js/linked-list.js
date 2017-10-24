'use strict';

class Node {
    constructor (value) {
        this.next = null
        this.value = value
    }
}

class LinkedList() {
    constructor(head, length) {
        this.head = null
        this.length = 0
    }
}

LinkedList.prototype.push = function(value) {
    let node = new Node(value)

    node.next = this.head
    this.head = node
    this.length += 1
    return this
}

LinkedList.prototype.pop = function() {
    deleted = this.head
    this.head = this.head.next
    this.length -= 1
    return deleted
}

LinkedList.prototype.size = function() {
    return this.length
}

LinkedList.prototype.search = function(target) {
    current = this.head
    while current.value != target {
        if current.next == null {
            return null
        } else {
            current = current.next
        }
    }

    return current

LinkedList.prototype.remove = function(target) {
    current = this.head
    next = current.next
    if current.value == target {
        this.pop()
        return current
    }
    
    while next.value != target {
        if next.next == null {
            console.log('not found')
            return null
        } else {
            current = next
            next = current.next
        }
    }
    this.length -= 1
    return this
}
