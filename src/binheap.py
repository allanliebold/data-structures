"""Implementation of a Max Binary Heap."""


class Heap(object):
    """Create Heap class object."""

    def __init__(self, iterable=()):
        """Initialization of Heap."""
        self.contents = []
        self._size = 0
        if isinstance(iterable, (tuple, list)):
            for i in iterable:
                self.push(i)

    def push(self, data):
        """Add new value to end of contents and sorts contents."""
        if data in self.contents:
            raise ValueError('Number already in list.')
        self.contents.append(data)
        self._size += 1
        if len(self.contents) == 1:
            return
        else:
            self.heapify()

    def pop(self):
        """Remove the value at the top of the heap and sort."""
        if self._size == 0:
            raise IndexError('Heap empty.')

        if self._size == 1:
            self.contents = []
        elif self._size == 2:
            del self.contents[0]
        else:
            del self.contents[0]
            self.heapify()
        self._size -= 1
        return

    def heapify(self):
        """Re-sort heap in proper order."""
        i = len(self.contents) - 1
        parent = (i - 1) // 2
        while i > 0:
            if self.contents[i] > self.contents[parent]:
                self.contents[i], self.contents[parent] = \
                    self.contents[parent], self.contents[i]

            i, parent = parent, (i - 1) // 2
        return
