"""The linked list data sturcture."""


class Node(object):  # pragma: no cover
    """The node object holds the data and is aware of the next node in the chain."""

    def __init__(self, val):
        """Makes a node object."""
        self.val = val
        self.next_node = None


class LinkedList(object):
    """Holds the linked list methods."""

    def __init__(self, itter=None):
        """Makes a LinkedList object."""
        self.head = None
        self.length = 0
        if type(itter) in [list, tuple, str]:
            for thing in itter:
                self.push(thing)
        elif itter is not None:
            raise TypeError('Please input only a list, tuple or string.')

    def push(self, val=None):
        """Create a new node."""
        if val is None:
            raise ValueError('Must be called with a value.')
        new_node = Node(val)
        new_node.next_node = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        """Removes and returns the head o the LinkedList."""
        currnode = self.head
        if currnode is None:
            raise IndexError('The list is empty please push somthing.')
        self.length -= 1
        self.head = currnode.next_node
        return currnode

    def size(self):
        """Return the size of the linked list."""
        return self.length

    def search(self, val=None):
        """ Finds and returns a node for any value."""
        currnode = self.head
        if val is None:
            raise ValueError('Must be called with a value.')
        while currnode:
            if val == currnode.val:
                return currnode
            currnode = currnode.next_node
        return None

    def remove(self, node):
        """Finds and removes a node from the linked list."""
        currnode = self.head
        prenode = None
        if currnode is None:
            raise ValueError('Node not in linked list.')
        while currnode != node:
            prenode = currnode
            currnode = currnode.next_node
            if currnode is None:
                raise ValueError('Node not in linked list.')
        if prenode is None:
            self.head = currnode.next_node
        else:
            prenode.next_node = currnode.next_node
        currnode.next_node = None
        self.length -= 1

    def display(self):
        """Desplaies the linked list as a tuple."""
        output = ''
        currnode = self.head
        while currnode:
                output = output + str(currnode.val)
                output = output + ' '
                currnode = currnode.next_node
        output = output.strip().replace(' ', ', ')
        output = '({})'.format(output)
        return output

    def __len__(self):
        """Returns the length of the linked list."""
        return self.length

    def __repr__(self):
        """Prints the linked list."""
        return self.display()
