import sys

class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val):
        self.stack.append(val)
        minim = min(val, self.mini[-1] if  self.mini else val)
        self.mini.append(minim)
        # if self.mini[-1] >= val:
        #     self.mini.append(val)

    def pop(self):
        top = self.stack.pop()
        if top == self.mini[-1]:
            self.mini.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.mini[-1]

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Output: -3
min_stack.pop()
print(min_stack.top())     # Output: 0
print(min_stack.getMin())  # Output: -2
