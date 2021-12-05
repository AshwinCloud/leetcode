# PROBLEM STATEMENT
# https://leetcode.com/problems/fibonacci-number/
# The Fibonacci numbers, commonly denoted F(n) form a sequence,
# called the Fibonacci sequence, such that each number is the
# sum of the two preceding ones, starting from 0 and 1. That is,
class Solution:
    def fib(self, n: int) -> int:
        return self.fibDP(n)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def fibDP(self, n: int) -> int:
        def helper(n: int, memory={0: 0, 1: 1}):
            if n in memory:
                return memory[n]
            else:
                memory[n] = helper(n - 1, memory) + helper(n - 2, memory)
                return memory[n]

        return helper(n)