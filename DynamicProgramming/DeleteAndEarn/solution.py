# PROBLEM STATEMENT
# https://leetcode.com/problems/delete-and-earn/
# You are given an integer array nums.
# You want to maximize the number of points you get by performing the following operation any number of times:
# Pick any nums[i] and delete it to earn nums[i] points.
# Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        return self.deleteAndEarnDP(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def deleteAndEarnDP(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            n = len(nums)
            freqs = [0] * 10001
            max_num = -1

            for num in nums:
                max_num = max(max_num, num)
                freqs[num] += 1

            points_i_minus_2, points_i_minus_1 = 0, freqs[1]

            for i in range(2, max_num + 1):
                points_i_minus_2, points_i_minus_1 = points_i_minus_1, max(freqs[i] * i + points_i_minus_2,
                                                                           points_i_minus_1)

            return points_i_minus_1