# PROBLEM STATEMENT
# https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArrayDP(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxSubArrayDP(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum