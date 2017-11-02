"""Implementation of a priority queue."""


class PriQ(object):
    """Create priority queue class object."""

    def __init__(self):
        """Initialization of Pri_Q class."""
        self.pri_dict = {}

    def insert(self, data, priority=0):
        """Add value to queue with data and optional priority level."""
        if not isinstance(data, (int, float)):
            raise TypeError('Priority must be a number.')

        if priority in self.pri_dict:
            self.pri_dict[priority].append(data)
        else:
            self.pri_dict[priority] = [data]

    def pop(self):
        """Remove value from queue in order of highest priority.

        If more than one value of same priority, first in first out.
        """
        if self.pri_dict == {}:
            raise IndexError('Priority Queue is empty.')
        high_pri = max(self.pri_dict)
        del_val = self.pri_dict[high_pri][0]
        del self.pri_dict[high_pri][0]
        if len(self.pri_dict[high_pri]) == 0:
            del self.pri_dict[high_pri]
        return del_val
