# PROBLEM STATEMENT
# https://leetcode.com/problems/longest-increasing-subsequence/
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing
# the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.lengthOfLISBS(nums)

    # Time Complexity: O(n * n)
    # Space Complexity: O(n)
    def lengthOfLISDP(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def lengthOfLISBS(self, nums: List[int]) -> int:
        def binarySearch(bs_list: List[int], n: int) -> int:
            left = 0
            right = len(bs_list) - 1
            index = len(bs_list)

            while left <= right:
                mid = (left + right) // 2
                if n <= bs_list[mid]:
                    right = mid - 1
                    index = min(index, mid)
                else:
                    left = mid + 1

            return -1 if index == len(bs_list) else index

        bs_list = []
        for i in range(len(nums)):
            index = binarySearch(bs_list, nums[i])
            if index == -1:
                bs_list.append(nums[i])
            else:
                bs_list[index] = nums[i]

        return len(bs_list)