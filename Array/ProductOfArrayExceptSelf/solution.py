# PROBLEM STATEMENT
# https://leetcode.com/problems/product-of-array-except-self/
# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.productExceptSelfConstantSpace(nums)

    # Time Complexity: O(n) where n is the size of nums
    # Space Complexity: O(n) and O(1) with and without including the extra space for result
    def productExceptSelfConstantSpace(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = nums[i - 1] * result[i - 1]

        rightProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * rightProduct
            rightProduct *= nums[i]

        return result

    # Time Complexity: O(n) where n is the size of nums
    # Space Complexity: O(n) with and without including the extra space for result
    def productExceptSelfArray(self, nums: List[int]) -> List[int]:
        result, left, right = [1] * len(nums), [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]

        for i in range(len(nums)):
            result[i] = left[i] * right[i]

        return result