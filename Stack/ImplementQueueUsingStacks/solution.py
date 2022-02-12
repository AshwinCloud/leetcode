# Implement a first in first out (FIFO) queue using only two stacks.
# The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class:
# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size,
# and is empty operations are valid.
# Depending on your language, the stack may not be supported natively.
# You may simulate a stack using a list or deque (double-ended queue)
# as long as you use only a stack's standard operations.

class MyQueue:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.front = None

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def push(self, x: int) -> None:
        if not self.queue1:
            self.front = x
        self.queue1.append(x)

    # Time Complexity: O(n) worst case and O(1) amortized where n is the size of the queue
    # Space Complexity: O(1)
    def pop(self) -> int:
        if not self.queue2:
            while self.queue1:
                self.queue2.append(self.queue1.pop())
        return self.queue2.pop() if self.queue2 else None

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def peek(self) -> int:
        return self.queue2[-1] if self.queue2 else self.front

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def empty(self) -> bool:
        return not self.queue1 and not self.queue2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()