# PROBLEM STATEMENT
# https://leetcode.com/problems/binary-search/
# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchBinaryIterative(nums, target)

    def searchBinaryIterative(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        else:
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + ((right - left) // 2)
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid

            return -1
