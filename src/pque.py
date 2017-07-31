"""Implementation of a priority queue sorted by positive numbers."""


class pque(object):
    """Define all the atributes and methods in the pque class."""

    def __init__(self):
        """Inits the pque instance."""
        self._que = []

    def insert(self, val, priority=0):
        """Add a value to the pque and priority is set to 0 as defalt."""
        new_pair = (priority, val)
        if type(new_pair[0]) not in [int, float]:
            raise ValueError('Please input a number for the priority.')
        if len(self._que) == 0:
            self._que.append(new_pair)
        else:
            flag = 0
            for i in range(len(self._que)):
                if self._que[i][0] < new_pair[0]:
                    self._que.insert(i, new_pair)
                    flag = 1
                    break
            if flag == 0:
                self._que.append(new_pair)

    def peek(self):
        """Return the highest priority item in pque."""
        if len(self._que) > 0:
            return self._que[0][1]
        raise IndexError("The pque is empty.")

    def pop(self):
        """Remove and return highest priority item in pque."""
        if len(self._que) > 0:
            popped = self._que.pop(0)
            return popped[1]
        raise IndexError("The pque is empty.")
