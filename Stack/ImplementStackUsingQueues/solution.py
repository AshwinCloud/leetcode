# PROBLEM STATEMENT
# https://leetcode.com/problems/implement-stack-using-queues/
# Implement a last-in-first-out (LIFO) stack using only two queues.
# The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back,
# peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively.
# You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

class MyStack:

    def __init__(self):
        self.q = []

    # Time Complexity: O(n) where n is the size of q
    # Space Complexity: O(1)
    def push(self, x: int) -> None:
        self.q.insert(0, x)

        sz = len(self.q)
        while sz > 1:
            self.q.insert(0, self.q.pop())
            sz -= 1

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def pop(self) -> int:
        return self.q.pop()

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def top(self) -> int:
        return self.q[len(self.q) - 1]

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def empty(self) -> bool:
        return len(self.q) == 0

    # Your MyStack object will be instantiated and called as such:
    # obj = MyStack()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.empty()