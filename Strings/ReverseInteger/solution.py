# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
class Solution:
    def reverse(self, x: int) -> int:
        return self.reverse1(x)
    
    def reverse1(self, x: int) -> int:
        max_int = (2 ** 31) - 1
        
        is_positive = False if x < 0 else True
        reversed_num = 0
        num = abs(x)
        
        while num > 0:
            if max_int // 10 < reversed_num:
                return 0
            elif is_positive and max_int // 10 == reversed_num and max_int % 10 < num % 10:
                return 0
            elif not is_positive and max_int // 10 == reversed_num and (max_int % 10) + 1 < num % 10:
                return 0
            else:
                reversed_num = (reversed_num * 10) + num % 10
                num //= 10
            
        return reversed_num if is_positive else reversed_num * -1