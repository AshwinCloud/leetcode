# PROBLEM STATEMENT
# https://leetcode.com/problems/number-of-islands/
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
# return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.numIslandsBFS(grid)

    # Time Complexity: O(n * m) where n and m are the rows and columns in the grid
    # Space Complexity: O(n * m)
    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        def dfs(grid: List[List[str]], visited: List[List[bool]], row: int, col: int) -> bool:
            if (row < 0 or
                    row >= len(grid) or
                    col < 0 or
                    col >= len(grid[0]) or
                    visited[row][col] or
                    grid[row][col] != "1"):
                return False
            else:
                visited[row][col] = True
                for (i, j) in [(0, - 1), (0, 1), (-1, 0), (1, 0)]:
                    dfs(grid, visited, row + i, col + j)
                return True

        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]
        num_islands = 0

        for r in range(rows):
            for c in range(cols):
                num_islands += 1 if dfs(grid, visited, r, c) else 0

        return num_islands
    
    # Time Complexity: O(n * m) where n and m are the rows and columns in the grid
    # Space Complexity: O(n * m)
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        def bfs(grid: List[List[str]], visited: List[List[bool]], row: int, col: int) -> bool:
            if (visited[row][col] or
                    grid[row][col] != "1"):
                return False
            else:
                q = []
                q.append((row, col))

                while q:
                    r, c = q.pop(0)
                    visited[r][c] = True
                    for (i, j) in [(0, - 1), (0, 1), (-1, 0), (1, 0)]:
                        # print(f"r: {r} c: {c}, i: {i}, j: {j}")
                        if 0 <= r + i < len(grid) and 0 <= c + j < len(grid[0]) and not visited[r + i][c + j] and \
                                grid[r + i][c + j] == "1":
                            q.append((r + i, c + j))
                            visited[r + i][c + j] = True
                return True

        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]
        num_islands = 0

        for r in range(rows):
            for c in range(cols):
                num_islands += 1 if bfs(grid, visited, r, c) else 0

        return num_islands