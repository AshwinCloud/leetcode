# PROBLEM STATEMENT
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
# of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return self.minSubArrayLenSlidingArray(target, nums)

    # Time Complexity: O(n) where n is the size of nums
    # Space Complexity: O(1)
    def minSubArrayLenSlidingArray(self, target: int, nums: List[int]) -> int:
        l = currentSum = 0
        minLen = len(nums) + 1

        for r in range(len(nums)):
            currentSum += nums[r]

            while currentSum >= target:
                minLen = min(minLen, r - l + 1)
                currentSum -= nums[l]
                l += 1

        return minLen if minLen <= len(nums) else 0