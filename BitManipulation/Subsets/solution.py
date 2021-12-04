# PROBLEM STATEMENT
# https://leetcode.com/problems/subsets/
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subsetsBitwise(nums)

    # Time Complexity: O(2^n) where n is the length of nums
    # Space Complexity: O(2^n) where n is the length of nums
    def subsetsBitwise(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = 1 << len(nums)

        for i in range(n):
            subset = []

            for j in range(len(nums)):
                if (i >> j) & 1 == 1:
                    subset.append(nums[j])
            subsets.append(subset)
        return subsets