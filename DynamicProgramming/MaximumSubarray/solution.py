# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArrayOnePass(nums)
    
    def maxSubArrayOnePass(self, nums: List[int]) -> int:
        local_max_sum = nums[0]
        global_max_sum = nums[0]
        for n in nums[1:]:
            local_max_sum = max(local_max_sum + n, n)
            global_max_sum = max(global_max_sum, local_max_sum)
        return global_max_sum