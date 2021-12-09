# PROBLEM STATEMENT
# https://leetcode.com/problems/jump-game/
# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.canJumpDP(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def canJumpDP(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        else:
            max_jump_to = nums[0]

            for i in range(len(nums)):
                if max_jump_to <= i and nums[i] == 0:
                    return False

                max_jump_to = max(max_jump_to, nums[i] + i)

                if max_jump_to >= len(nums) - 1:
                    return True

            return False