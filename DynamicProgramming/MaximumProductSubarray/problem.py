# PROBLEM STATEMENT
# https://leetcode.com/problems/maximum-product-subarray/
# Given an integer array nums,
# find a contiguous non-empty subarray within the array that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# A subarray is a contiguous subsequence of the array.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return self.maxProductDP(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProductDP(self, nums: List[int]) -> int:
        result = max(nums)
        curMaxP = curMinP = 1

        for n in nums:
            curMaxP, curMinP = max(n, n * curMaxP, n * curMinP), min(n, n * curMaxP, n * curMinP)
            result = max(result, curMaxP)

        return result