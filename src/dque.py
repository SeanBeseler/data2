"""Implements the dequeue data structure."""
from double_linked_list import DoubleLinkedList


class dque(object):
    """Set attributes and methods of dque object."""

    def __init__(self):
        """Initialize deque using double linked list."""
        self._dque = DoubleLinkedList()

    def append(self, val):
        """Add value to the head of a dque."""
        self._dque.append(val)

    def appendleft(self, val):
        """Add value to the tail of a dque."""
        self._dque.push(val)

    def pop(self):
        """Remove the back of the deque."""
        if not self._dque.tail:
            raise IndexError('The deque is empty.')
        node = self._dque.shift()
        return node

    def popleft(self):
        """Remove the front of the dque."""
        if not self._dque.head:
            raise IndexError('The Deque is empty.')
        node = self._dque.pop()
        return node

    def peek(self):
        """Return the dque tail."""
        if self._dque.tail is None:
            return None
        return self._dque.tail.val

    def peekleft(self):
        """Return the dque head."""
        if self._dque.head is None:
            return None
        return self._dque.head.val

    def size(self):
        """Return the size of the dque."""
        return self._dque.size

    def __len__(self):
        """Return the size of dque."""
        return self._dque.size
