# PROBLEM STATEMENT
# https://leetcode.com/problems/sum-of-two-integers/
# Given two integers a and b, return the sum of the two integers without using the operators + and -.
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return self.getSum1(a, b)

    def getSum1(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask:
            a, b = a ^ b, (a & b) << 1
        return a & mask if b > 0 else a