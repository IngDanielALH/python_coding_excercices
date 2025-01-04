"""
Design a stack that supports push, pop, top, and retrieving the maximum element in constant time.

    push(x): Pushes an element x onto the stack.
    pop(): Removes the element on top of the stack.
    top(): Gets the element on the top of the stack.
    getMax(): Retrieves the maximum element in the stack.
Example:
    Input:
    push(5)
    push(1)
    push(5)
    getMax()
    pop()
    getMax()
    top()

Output:
    5
    5
    1

Explanation:
    Push 5 -> Stack: [5]
    Push 1 -> Stack: [5, 1]
    Push 5 -> Stack: [5, 1, 5]
    getMax() -> Maximum is 5.
    pop() -> Remove top element (5) -> Stack: [5, 1]
    getMax() -> Maximum is now 5.
    top() -> Top element is 1.
"""


class Stack:
    def __init__(self):
        self.stack_arr = []
        self.max_stack = []

    def push(self, value):
        self.stack_arr.append(value)
        # Update max stack
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack_arr:
            print("Stack is empty. Nothing to pop.")
            return None
        popped = self.stack_arr.pop()
        # Update max stack if necessary
        if popped == self.max_stack[-1]:
            self.max_stack.pop()
        return popped

    def top(self):
        if not self.stack_arr:
            print("Stack is empty. No top element.")
            return None
        return self.stack_arr[-1]

    def get_max(self):
        if not self.max_stack:
            print("Stack is empty. No maximum value.")
            return None
        return self.max_stack[-1]

