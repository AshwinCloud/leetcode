# PROBLEM STATEMENT
# https://leetcode.com/problems/power-of-two/
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return self.isPowerOfTwoBin(n)

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def isPowerOfTwoBin(self, n: int) -> bool:
        return n != 0 and (n & (n - 1)) == 0