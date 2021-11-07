# PROBLEM STATEMENT
# https://leetcode.com/problems/3sum/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.threeSumSort(nums)

    def threeSumSort(self, nums: List[int]) -> List[List[int]]:
        threeSumSet = set()
        nums.sort()

        for i in range(len(nums)):
            compliment = 0 - nums[i]
            start = i + 1
            end = len(nums) - 1

            while start < end:
                if nums[start] + nums[end] < compliment:
                    start += 1
                elif nums[start] + nums[end] > compliment:
                    end -= 1
                else:
                    threeSumSet.add((nums[i], nums[start], nums[end]))
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
        return list(threeSumSet)