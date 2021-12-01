# PROBLEM STATEMENT
# https://leetcode.com/problems/combinations/
# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
# You may return the answer in any order.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combineBacktrack(n, k)

    # Time Complexity: O(nCk)
    # Space Complexity: O(nCk) for the result, O(1) for additional space
    def combineBacktrack(self, n: int, k: int) -> List[List[int]]:
        def backtrack(n: int, k: int, start: int = 1, comb: List[int] = [], result: List[List[int]] = []):
            if len(comb) == k:
                result.append(comb)
            else:
                for i in range(start, n + 1):
                    backtrack(n, k, i + 1, comb + [i], result)

            return result

        return backtrack(n, k)