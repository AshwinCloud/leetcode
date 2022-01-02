# PROBLEM STATEMENT
# https://leetcode.com/problems/product-of-array-except-self/
# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.productExceptSelfConstantSpace(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def productExceptSelfConstantSpace(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def productExceptSelfArray(self, nums: List[int]) -> List[int]:
        prefix = nums.copy()
        postfix = nums.copy()

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        output = [1] * len(nums)
        output[0] = postfix[1]
        output[len(nums) - 1] = prefix[len(nums) - 2]

        for i in range(1, len(nums) - 1):
            output[i] = prefix[i - 1] * postfix[i + 1]

        return output