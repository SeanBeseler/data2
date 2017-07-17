"""Implementation of the double linked list data structure."""


class Node(object):
    """Hold the data for the double linked list."""

    def __init__(self, val, next_node=None, prev_node=None):
        """Makes a new node object."""
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node


class DoubleLinkedList(object):
    """Holds the order of the double linked list."""

    def __init__(self):
        """Makes a new double linked list."""
        self.tail = None
        self.head = None
        self.size = 0

    def push(self, val=None):
        """pushes new node."""
        if val is None:
            raise ValueError('Input a value when you call this function.')
        new_node = Node(val, self.head)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next_node = None
            self.size += 1
        else:
            self.head.prev_node = new_node
            self.head = new_node
            self.size += 1

    def append(self, val=None):
        """Appends new node to the double linked list."""
        if val is None:
            raise ValueError('Input a value when you call this function.')
        new_node = Node(val, None, self.tail)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev_node = None
            self.size += 1
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.size += 1

    def pop(self):
        """Returns the head of the double linked list."""
        curr_node = self.head
        if curr_node is None:
            raise IndexError('List is empty.')
        if curr_node.next_node is not None:
            self.head = curr_node.next_node
            self.head.prev_node = None
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        return curr_node

    def shift(self):
        """Returns and removes the node from tail of double linked list."""
        curr_node = self.tail
        if curr_node is None:
            raise IndexError('List is empty.')
        if curr_node.prev_node is not None:
            self.tail = curr_node.prev_node
            self.tail.next_node = None
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        return curr_node.val

    def remove(self, val):
        """Finds and removes a node in the double linked list."""
        curr_item = self.head
        while curr_item.val != val:
            curr_item = curr_item.next_node
            if curr_item is None:
                raise ValueError('Node not in doubly linked list.')
        if curr_item.prev_node is None:
            self.head = curr_item.next_node
            if self.head is not None:
                self.head.prev_node = None
            else:
                self.tail = None
        elif curr_item.next_node is None:
            self.tail = curr_item.prev_node
            self.tail.next_node = None
        else:
            curr_item.prev_node.next_node = curr_item.next_node
            curr_item.next_node.prev_node = curr_item.prev_node
        self.size -= 1

    def __len__(self):
        """Return the size of a double linked list."""
        return self.size
