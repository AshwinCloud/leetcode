# PROBLEM STATEMENT
# https://leetcode.com/problems/combination-sum/
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combinationSumDFS(candidates, target)

    # Time Complexity: O(2^k) where k is the target
    # Space Complexity:
    def combinationSumDFS(self, candidates: List[int], target: int) -> List[List[int]]:

        def helper(candidates: List[int], target: int, i: int, current: List[int] = [], total: int = 0,
                   result: List[List[int]] = []) -> List[List[int]]:
            if target == total:
                result.append(current.copy())
                return result
            elif target < total or i >= len(candidates):
                return result
            else:
                current.append(candidates[i])
                helper(candidates, target, i, current, total + candidates[i], result)
                current.pop()
                helper(candidates, target, i + 1, current, total, result)
                return result

        return helper(candidates, target, 0)