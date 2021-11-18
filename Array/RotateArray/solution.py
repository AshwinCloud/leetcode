# PROBLEM STATEMENT
# https://leetcode.com/problems/rotate-array/
# Given an array, rotate the array to the right by k steps, where k is non-negative.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.rotateReverse(nums, k)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def rotateReverse(self, nums: List[int], k: int) -> None:
        def reverse(nums: List[int], start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)