# PROBLEM STATEMENT
# https://leetcode.com/problems/max-area-of-island/
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return self.maxAreaOfIslandDFS(grid)

    # Time Complexity: O(n^2)
    # Space Complexity: 0(1)
    def maxAreaOfIslandDFS(self, grid: List[List[int]]) -> int:
        def helper(grid: List[List[int]], sr: int, sc: int) -> int:
            area = 0
            if 0 <= sr < len(grid) and 0 <= sc < len(grid[0]) and grid[sr][sc] == 1:
                grid[sr][sc] = 0
                area += 1
                area += helper(grid, sr - 1, sc)
                area += helper(grid, sr + 1, sc)
                area += helper(grid, sr, sc - 1)
                area += helper(grid, sr, sc + 1)
            return area

        return max(helper(grid, i, j)
                   for i in range(len(grid))
                   for j in range(len(grid[0])))