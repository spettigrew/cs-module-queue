"""
Add a peek method to the Stack class below. The peek method should return the value of the node that is at the top of the stack without actually removing it from the stack.
"""
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        # create new node with data
        new_node = LinkedListNode(data)
        # set current top to new node's next
        new_node.next = self.top
        # reset the top pointer to the new node
        self.top = new_node
        # don't need to return anything with a push

    def pop(self):
        # make sure stack is not empty
        if self.top is not None:
            # store popped node
            popped_node = self.top
            # reset top pointer to next node
            self.top = popped_node.next
            # return the value from the popped node
            return popped_node.data

    def peek(self):
        return self.top[-1]