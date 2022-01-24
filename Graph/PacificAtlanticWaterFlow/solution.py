# PROBLEM STATEMENT
# https://leetcode.com/problems/pacific-atlantic-water-flow/
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
# The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells.
# You are given an m x n integer matrix heights where heights[r][c]
# represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring
# cells directly north, south, east, and west if the neighboring cell's height is
# less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        return self.pacificAtlanticDFS(heights)

    # Time Complexity: O(n * m)) where n and m are the rows and columns in heights
    # Space Complexity: O(n * m)
    def pacificAtlanticDFS(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(heights: List[List[int]], canFlow: List[List[bool]], row, col, previousHeight: int):
            if (row < 0 or
                    row >= len(heights) or
                    col < 0 or
                    col >= len(heights[0]) or
                    canFlow[row][col] or
                    heights[row][col] < previousHeight):
                return
            else:
                canFlow[row][col] = True

                for (r, c) in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    dfs(heights, canFlow, row + r, col + c, heights[row][col])

                return

        rows = len(heights)
        cols = len(heights[0])

        canFlowToPacific = [[False] * cols for _ in range(rows)]
        canFlowToAtlantic = [[False] * cols for _ in range(rows)]
        canFlowToBoth = []

        for c in range(cols):
            dfs(heights, canFlowToPacific, 0, c, heights[0][c])
            dfs(heights, canFlowToAtlantic, rows - 1, c, heights[rows - 1][c])

        for r in range(rows):
            dfs(heights, canFlowToPacific, r, 0, heights[r][0])
            dfs(heights, canFlowToAtlantic, r, cols - 1, heights[r][cols - 1])

        for r in range(rows):
            for c in range(cols):
                if canFlowToPacific[r][c] and canFlowToAtlantic[r][c]:
                    canFlowToBoth.append((r, c))

        return canFlowToBoth