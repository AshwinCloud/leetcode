# PROBLEM STATEMENT
# https://leetcode.com/problems/squares-of-a-sorted-array/
# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return self.sortedSquaresLinearTwoPointers(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def sortedSquaresLinearTwoPointers(self, nums: List[int]) -> List[int]:
        squares = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        index = len(nums) - 1

        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                squares[index] = nums[left] * nums[left]
                left += 1
            else:
                squares[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        return squares

    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def squareAndSort(self, nums: List[int]) -> List[int]:
        squares = [n * n for n in nums]
        squares.sort()
        return squares