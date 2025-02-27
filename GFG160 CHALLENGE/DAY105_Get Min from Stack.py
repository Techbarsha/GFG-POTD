class Solution:

    def __init__(self):
        # code here
        self.stack=[]
        self.min_stack=[]
    # Add an element to the top of Stack
    def push(self, x):
        # code here
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    # Remove the top element from the Stack
    def pop(self):
        # code here
        if self.stack:
            popped =  self.stack.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()
            

    # Returns top element of Stack
    def peek(self):
        # code here
        return self.stack[-1] if self.stack else -1

    # Finds minimum element of Stack
    def getMin(self):
        # code here
        return self.min_stack[-1] if self.min_stack else -1
