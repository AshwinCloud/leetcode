# PROBLEM STATEMENT
# https://leetcode.com/problems/self-dividing-numbers/
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return self.selfDividingNumbers1(left, right)

    # Time Complexity: O(n * m) where n is the number of numbers between left and right, m is the average number of digits in each number
    # Space Complexity: O(n) including the size of the return value
    def selfDividingNumbers1(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num: int) -> bool:
            temp_num = num

            while temp_num:
                digit = temp_num % 10

                if digit == 0 or num % digit != 0:
                    return False

                temp_num //= 10

            return True

        ret_list = []
        for i in range(left, right + 1):
            if isSelfDividing(i):
                ret_list.append(i)

        return ret_list