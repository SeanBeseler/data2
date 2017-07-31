"""Implements the que data structure."""
from double_linked_list import DoubleLinkedList


class que(object):
    """Set the que object."""

    def __init__(self):
        """Inits the  que using the double linkedlist."""
        self._que = DoubleLinkedList()

    def enqueue(self, val):
        """Add value to a que."""
        self._que.append(val)

    def dequeue(self):
        """Remove the head from the que and returns the val."""
        node = self._que.pop()
        return node.val

    def peek(self):
        """Return the que head node."""
        return self._que.head

    def size(self):
        """Return the size of the que."""
        return self._que.size

    def __len__(self):
        """Return the size of que."""
        return self._que.size
