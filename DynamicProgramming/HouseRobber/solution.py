#PROBLEM STATEMENT
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.robDynamic(nums)
    
    def robDynamic(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            house = [0] * len(nums)
            house[0] = nums[0]
            house[1] = max(nums[0], nums[1])
            
            for i in range(2, len(nums)):
                house[i] = max(nums[i] + house[i-2], house[i-1])
                
            return house[len(nums)-1]