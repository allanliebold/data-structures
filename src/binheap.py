"""Implementation of a Max Binary Heap."""


class Heap(object):
    """Create Heap class object."""

    def __init__(self, iterable=()):
        """Initialization of Heap."""
        self.contents = []
        if isinstance(iterable, (tuple, list)):
            for i in iterable:
                self.push(i)

    def push(self, data):
        """Add new value to end of contents and sorts contents."""
        self.contents.append(data)
        if len(self.contents) == 1:
            print('First: {}'.format(self.contents))
            return
        else:
            print(self.contents)
            i = len(self.contents) - 1
            parent = (i - 1) // 2
            print('i: {}'.format(i))
            print('Parent: {}'.format(parent))
            while i > 0:
                if self.contents[i] > self.contents[parent]:
                    self.contents[i], self.contents[parent] = \
                        self.contents[parent], self.contents[i]

                i -= 1
                parent = (i - 1) // 2
                print(self.contents)
            return
