# PROBLEM STATEMENT
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]]
# 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.findMinBSInflectionPoint(nums)

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def findMinBS(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def findMinBSInflectionPoint(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]
        else:
            left = 0
            right = len(nums) - 1
            mid = (left + right) // 2

            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    return nums[mid + 1]
                elif nums[mid - 1] > nums[mid]:
                    return nums[mid]

                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            return nums[mid]