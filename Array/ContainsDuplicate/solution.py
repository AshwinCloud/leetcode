# 217. Contains Duplicate
# PROBLEM STATEMENT
# https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return self.containsDuplicateSet(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def containsDuplicateSet(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def containsDuplicateSort(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False