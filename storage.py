class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        """ Store the data, and set next to None"""

    def __str__(self):
        """ Return a string representation of the data """
        return str(self.data)


class Storage:
    def __init__(self):
        """ Creates an empty Storage class. Sets head to None. """
        self.head = None

    def push(self, data):
        """ Create a Node to hold the data, then put it at the head of the list. """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """ Remove the head Node and return its data. """
        # deque?
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next


        return data

    def peek(self):
        """ Return the data from the head Node, without removing it. """

        return self.head.data

    @property
    def isempty(self):
        """ Return True if the list is empty, otherwise False """
        return self.head is None
