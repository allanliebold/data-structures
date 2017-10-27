"""Implementation of Queue."""
from dll import Dll


class Queue(object):
    """Queue Class."""

    def __init__(self):
        """Queue initiliazation."""
        self._dll = Dll()
