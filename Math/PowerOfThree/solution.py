# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            m = n
            while m > 0 and m % 3 == 0:
                m //= 3            
            return m == 1