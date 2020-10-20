"""
Add a peek method to the Stack class. The peek method should return the value of the top item in the stack without actually removing it from the stack.
"""
class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
        return

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            print("There is nothing to pop")
        return
    
    def peek(self):
        return self.data[-1]