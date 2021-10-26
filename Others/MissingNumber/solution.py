# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return self.missingNumberSummationOverflow(nums)
    
    def missingNumberSummation(self, nums: List[int]) -> int:
        expected_sum = ((len(nums)) * (len(nums) + 1)) // 2
        actual_sum = sum(nums)
        return (expected_sum - actual_sum )
    
    def missingNumberSummationOverflow(self, nums: List[int]) -> int:
        total = 0
        i = 0
        for i in range(len(nums)):
            total = total + i - nums[i]
        return total + i + 1