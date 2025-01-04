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