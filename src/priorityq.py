"""Implementation of a priority queue."""


class PriQ(object):
    """Create priority queue class object."""

    def __init__(self):
        """Initialization of Pri_Q class."""
        self.pri_dict = {}

    def insert(self, data, priority=0):
        """Add value to queue with data and optional priority level."""
        if priority in self.pri_dict:
            self.pri_dict[priority].append(data)
        else:
            self.pri_dict[priority] = [data]
