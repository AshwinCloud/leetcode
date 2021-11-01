# PROBLEM STATEMENT
# https://leetcode.com/problems/search-insert-position/
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.searchInsertBinaryIterative(nums, target)

    def searchInsertBinaryRecursive(self, nums: List[int], target: int) -> int:
        def helper(nums: List[int], start: int, end: int, target: int) -> int:
            if not nums:
                return 0
            else:
                i = start + ((end - start) // 2)
                if start > end:
                    return start
                elif nums[i] < target:
                    return helper(nums, i + 1, end, target)
                elif nums[i] > target:
                    return helper(nums, start, i - 1, target)
                else:
                    return i

        return helper(nums, 0, len(nums) - 1, target)

    def searchInsertBinaryIterative(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return end + 1

    def searchInsertLinear(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == target or nums[i] > target:
                return i
            else:
                i += 1
        return i