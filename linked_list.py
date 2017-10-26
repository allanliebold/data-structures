"""Linked List."""


class Node(object):
    """Node Class."""

    def __init__(self, data):
        """Init."""
        self.next = None
        self.data = data


class LinkedList(object):
    """LinkedList Class."""

    def __init__(self, iterable=()):
        """Init."""
        self.head = None
        self._length = 0
        if isinstance(iterable, (tuple, list)):
            for i in iterable:
                self.push(i)
        else:
            self.push(iterable)

    def push(self, data):
        """Push method."""
        new = Node(data)
        new.next = self.head
        self.head = new
        self._length += 1
        return new

    def pop(self):
        """Pop method."""
        if not self.head:
            return None
        else:
            deleted_node = self.head.data
            self.head = self.head.next
            self._length -= 1
            return deleted_node

    def size(self):
        """Size method."""
        return self._length

    def search(self, target):
        """Search method."""
        current_node = self.head
        while current_node.data != target:
            if current_node.next is None:
                raise ValueError('not found')
            else:
                current_node = current_node.next
        print(current_node.data)
        return current_node

    def remove(self, target):
        """Remove method."""
        current_node = self.head
        next_node = current_node.next
        if current_node.data == target:
            self.pop()
            return current_node
        while next_node.data != target:
            if next_node.next is None:
                raise ValueError('Not found')
            else:
                current_node = next_node
                next_node = current_node.next
        current_node.next = next_node.next
        self.length -= 1
        return next_node

    def display(self):
        """Function Displays list."""
        list_contents = '('
        current_node = self.head
        list_contents += str(current_node.data)
        while current_node.next is not None:
            list_contents += ', ' + str(current_node.next.data)
            current_node = current_node.next
        list_contents += ')'
        return list_contents
        # the return above needs to be a unicode string

    def __len__(self):
        """Function overwrites built-in len function to show length."""
        return self._length

    def __str__(self):
        """Function overwrites built-in print to display list."""
        return self.display()
