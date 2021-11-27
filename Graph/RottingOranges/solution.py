# PROBLEM STATEMENT
# https://leetcode.com/problems/rotting-oranges/
# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        return self.orangesRottingBFS(grid)

    # Time Complexity: O(n*m) n=rows, m=columns
    # Space Complexity: O(n*m) n=rows, m=columns
    def orangesRottingBFS(self, grid: List[List[int]]) -> int:
        queue = []

        n_rows = len(grid)
        n_cols = len(grid[0])

        minutes = 0
        n_fresh = 0

        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 1:
                    n_fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col, minutes))
                else:
                    pass

        while n_fresh >= 0 and queue:
            row, col, minutes = queue.pop()
            for new_row, new_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= new_row < n_rows and 0 <= new_col < n_cols and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.insert(0, (new_row, new_col, minutes + 1))
                    n_fresh -= 1

        return minutes if n_fresh == 0 else -1