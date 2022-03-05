# 448. Find All Numbers Disappeared in an Array
# PROBLEM STATEMENT
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return self.findDisappearedNumbersNegation(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(n) and O(1) with and without including the space for result
    def findDisappearedNumbersNegation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            newIndex = abs(nums[i]) - 1
            if nums[newIndex] > 0:
                nums[newIndex] *= -1

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result