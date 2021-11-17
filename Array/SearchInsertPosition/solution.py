# PROBLEM STATEMENT
# https://leetcode.com/problems/search-insert-position/
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.searchInsertBinaryIterative(nums, target)

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def searchInsertBinaryRecursive(self, nums: List[int], target: int) -> int:
        def helper(nums: List[int], target: int, left: int, right: int) -> int:
            if not nums:
                return 0
            elif left > right:
                return left
            else:
                mid = left + ((right - left) // 2)

                if nums[mid] > target:
                    return helper(nums, target, left, mid - 1)
                elif nums[mid] < target:
                    return helper(nums, target, mid + 1, right)
                else:
                    return mid

        return helper(nums, target, 0, len(nums) - 1)

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def searchInsertBinaryIterative(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        else:
            left = 0
            right = len(nums) - 1
            mid = left + ((right - left) // 2)

            while left <= right:
                mid = left + ((right - left) // 2)
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid

            return left

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def searchInsertLinear(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        else:
            i = 0
            while i < len(nums) and nums[i] < target:
                i += 1
            return i