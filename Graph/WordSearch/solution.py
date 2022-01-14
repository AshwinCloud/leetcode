# PROBLEM STATEMENT
# https://leetcode.com/problems/word-search/
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.existDFS(board, word)

    # Time Complexity: O(m * n * 4^k) where m and n are the columns and rows in board, and k is the size of word
    # Space Complexity: O(m * n)
    def existDFS(self, board: List[List[str]], word: str) -> bool:
        def dfs(board: List[List[str]], word: str, word_index: int, board_row: int, board_col: int,
                visited: List[List[bool]]) -> bool:
            if word_index >= len(word):
                return True
            elif (0 > board_row or
                  board_row >= len(board) or
                  0 > board_col or
                  board_col >= len(board[0]) or
                  word[word_index] != board[board_row][board_col] or
                  visited[board_row][board_col]):
                return False
            else:
                visited[board_row][board_col] = True
                for (i, j) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    if dfs(board, word, word_index + 1, board_row + i, board_col + j, visited):
                        return True

                visited[board_row][board_col] = False
                return False

        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if dfs(board, word, 0, r, c, visited):
                    return True

        return False
