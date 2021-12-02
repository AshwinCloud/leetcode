# PROBLEM STATEMENT
# https://leetcode.com/problems/reverse-bits/
# Reverse bits of a given 32 bits unsigned integer.
class Solution:
    def reverseBits(self, n: int) -> int:
        return self.reverseBitsBin(n)

    # Time Complexity: O(m) where m is the number of bits in n
    # Space Complexity: O(1)
    def reverseBitsBin(self, n: int) -> int:
        num_bits = 32
        reversed_n = 0

        for i in range(num_bits):
            bit = (n >> i) & 1
            reversed_bit = bit << (num_bits - 1 - i)
            reversed_n |= reversed_bit

        return reversed_n