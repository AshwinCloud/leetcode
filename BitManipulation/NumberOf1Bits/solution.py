# PROBLEM STATEMENT
# https://leetcode.com/problems/number-of-1-bits/
# Write a function that takes an unsigned integer and
# returns the number of '1' bits it has (also known as the Hamming weight).
class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.hammingWeightBin(n)

    # Time Complexity: O(m) where n is the number of bits in integer n
    # Space Complexity: O(1)
    def hammingWeightBin(self, n: int) -> int:
        counter = 0
        while n > 0:
            if n & 1:
                counter += 1
            n = n >> 1

        return counter