# PROBLEM STATEMENT
# https://leetcode.com/problems/arithmetic-slices/
# An integer array is called arithmetic if it consists of at least three elements
# and if the difference between any two consecutive elements is the same.
# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.
# A subarray is a contiguous subsequence of the array.
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        return self.numberOfArithmeticSlicesDP(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def numberOfArithmeticSlicesDP(self, nums: List[int]) -> int:
        n = len(nums)
        dp = 0
        result = 0

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp += 1
                result += dp
            else:
                dp = 0

        return result