# PROBLEM STATEMENT
# https://leetcode.com/problems/triangle/
# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally,
# if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.minimumTotalDP(triangle)

    # Time Complexity: O(n*n)
    # Space Complexity: O(n)
    def minimumTotalDP(self, triangle: List[List[int]]) -> int:
        import sys
        num_rows = len(triangle)

        lookup = [sys.maxsize] * num_rows

        for col in range(len(triangle[num_rows - 1])):
            lookup[col] = triangle[num_rows - 1][col]

        for row in range(num_rows - 2, -1, -1):
            for col in range(len(triangle[row])):
                lookup[col] = triangle[row][col] + min(lookup[col], lookup[col + 1])

        return lookup[0]