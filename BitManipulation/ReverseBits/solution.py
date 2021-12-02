# PROBLEM STATEMENT
# https://leetcode.com/problems/reverse-bits/
# Reverse bits of a given 32 bits unsigned integer.
class Solution:
    def reverseBits(self, n: int) -> int:
        return self.reverseBitsBin(n)

    def reverseBitsBin(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (32 - i))

        return res