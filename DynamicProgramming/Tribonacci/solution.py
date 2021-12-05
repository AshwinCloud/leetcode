# PROBLEM STATEMENT
# https://leetcode.com/problems/n-th-tribonacci-number/
# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.
class Solution:
    def tribonacci(self, n: int) -> int:
        return self.tribonacciDPIterative(n)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def tribonacciDPRecursive(self, n: int) -> int:
        def helper(n: int, memory={0: 0, 1: 1, 2: 1}) -> int:
            if n not in memory:
                memory[n] = helper(n - 1, memory) + helper(n - 2, memory) + helper(n - 3, memory)

            return memory[n]

        return helper(n)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def tribonacciDPIterative(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            a, b, c = 0, 1, 1
            for _ in range(n - 2):
                a, b, c = b, c, a + b + c
            return c