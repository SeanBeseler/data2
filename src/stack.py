"""implments the stack"""
from linked_list import LinkedList


class Stack(object):
    """Is the start of the stack object class."""

    def __init__(self, itter=None):
        """Creates the new stack using the linked list."""
        self._linked_list = LinkedList(itter)
        self.head = self._linked_list.head

    def push(self, val):
        """Pushes an item on to the stack using the linked list ."""
        self.head = self._linked_list.head
        self._linked_list.push(val)
        self.head = self._linked_list.head

    def pop(self):
        """Pops the head of the stak using the linked list."""
        self.head = self._linked_list.head
        return self._linked_list.pop()

    def __len__(self):
        """Return the length of the Stack using the linked list."""
        return len(self._linked_list)
