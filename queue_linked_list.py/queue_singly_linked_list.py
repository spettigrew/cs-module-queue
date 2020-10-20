"""
Refactor the Queue class below by adding an `is_empty` method. 
After writing this method, refactor your other methods to use this method in your other methods.
"""
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = LinkedListNode(item)
        # check if queue is empty
        if self.is_empty is None:
            self.front = new_node
            self.rear = new_node
        else:
            # add new node to rear
            self.rear.next = new_node
            # reassign rear to new node
            self.rear = new_node

    def dequeue(self):
        # check if queue is empty
        if self.is_empty is not None:
            # keep copy of old front
            old_front = self.front
            # set new front
            self.front = old_front.next

        # check if the queue is now empty
        if self.front is None:
            # make sure rear is also None
            self.rear = None

        return old_front