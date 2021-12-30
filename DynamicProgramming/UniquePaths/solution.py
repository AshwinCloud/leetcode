# PROBLEM STATEMENT
# https://leetcode.com/problems/unique-paths/
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that
# the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.uniquePathsDPSpaceOptimized(m, n)

    # Time Complexity: O(m * n)
    # Space Complexity: O(n)
    def uniquePathsDPSpaceOptimized(self, m: int, n: int) -> int:
        prev_row = [1] * n

        for i in range(m - 2, -1, -1):
            curr_row = [0] * n
            for j in range(n - 1, -1, -1):
                if 0 <= i + 1 < m:
                    curr_row[j] += prev_row[j]
                if 0 <= j + 1 < n:
                    curr_row[j] += curr_row[j + 1]

            prev_row = curr_row

        return prev_row[0]

    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def uniquePathsDP(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[m - 1] = [1] * n

        for i in range(m - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                if 0 <= i + 1 < m:
                    dp[i][j] += dp[i + 1][j]
                if 0 <= j + 1 < n:
                    dp[i][j] += dp[i][j + 1]

        return dp[0][0]