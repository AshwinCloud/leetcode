# PROBLEM STATEMENT
# https://leetcode.com/problems/minimum-path-sum/
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.minPathSumDP1(grid)

    # Time Complexity: O(n*m) where n and m are the rows and cols of grid
    # Space Complexity: O(m)
    def minPathSumDP1(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [0] * cols

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if r == rows - 1:
                    dp[c] = grid[r][c] if c == cols - 1 else grid[r][c] + dp[c + 1]
                elif c == cols - 1:
                    dp[c] = grid[r][c] + dp[c]
                else:
                    dp[c] = grid[r][c] + min(dp[c], dp[c + 1])
        return dp[0]

    # Time Complexity: O(n*m) where n and m are the rows and cols of grid
    # Space Complexity: O(m)
    def minPathSumDP2(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [0] * cols

        for c in range(cols - 1, -1, -1):
            if c == cols - 1:
                dp[c] = grid[rows - 1][cols - 1]
            else:
                dp[c] = grid[rows - 1][c] + dp[c + 1]

        for r in range(rows - 2, -1, -1):
            for c in range(cols - 1, -1, -1):
                if c == cols - 1:
                    dp[c] = grid[r][c] + dp[c]
                else:
                    dp[c] = grid[r][c] + min(dp[c], dp[c + 1])

        return dp[0]