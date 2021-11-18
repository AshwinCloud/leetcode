# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.moveZeroesTwoPointers(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def moveZeroesTwoPointers(self, nums: List[int]) -> None:
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                non_zero_index += 1