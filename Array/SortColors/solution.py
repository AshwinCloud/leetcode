# PROBLEM STATEMENT
# https://leetcode.com/problems/sort-colors/
# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.sortColorsOnePass(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def sortColorsTwoPass(self, nums: List[int]) -> None:
        bucket = [0] * 3

        for n in nums:
            bucket[n] += 1

        index = 0
        for b in range(len(bucket)):
            for i in range(bucket[b]):
                nums[index] = b
                index += 1

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def sortColorsOnePass(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1

                if nums[i] != 1:
                    i -= 1

            i += 1