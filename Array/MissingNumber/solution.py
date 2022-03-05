# 268. Missing Number
# PROBLEM STATEMENT
# https://leetcode.com/problems/missing-number/
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return self.missingNumberSumOverflow(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def missingNumberSumOverflow(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result += (i - nums[i])
        return result

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def missingNumberSumNaive(self, nums: List[int]) -> int:
        expectedSum = 0
        for i in range(1, len(nums) + 1):
            expectedSum += i

        actualSum = 0
        for n in nums:
            actualSum += n

        return expectedSum - actualSum

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def missingNumberSummation(self, nums: List[int]) -> int:
        expected_sum = ((len(nums)) * (len(nums) + 1)) // 2
        actual_sum = sum(nums)
        return (expected_sum - actual_sum)