# PROBLEM STATEMENT
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.searchRangeBinary(nums, target)

    def searchRangeBinary(self, nums: List[int], target: int) -> List[int]:
        firstOccurence = self.searchFirstOccurenceBinary(nums, target)
        lastOccurence = self.searchLastOccurenceBinary(nums, target)
        return [firstOccurence, lastOccurence]

    def searchFirstOccurenceBinary(self, nums: List[int], target: int) -> List[int]:
        firstOccurence = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                firstOccurence = mid
                right = mid - 1

        return firstOccurence

    def searchLastOccurenceBinary(self, nums: List[int], target: int) -> List[int]:
        lastOccurence = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                lastOccurence = mid
                left = mid + 1

        return lastOccurence