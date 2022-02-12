# PROBLEM STATEMENT
# https://leetcode.com/problems/minesweeper/
# Let's play the minesweeper game (Wikipedia, online game)!
# You are given an m x n char matrix board representing the game board where:
# 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent mines
# (i.e., above, below, left, right, and all 4 diagonals),
# digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
# 'X' represents a revealed mine.
# You are also given an integer array click where click = [clickr, clickc]
# represents the next click position among all the unrevealed squares ('M' or 'E').
# Return the board after revealing this position according to the following rules:
# If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
# If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B'
# and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8')
# representing the number of adjacent mines.
# Return the board when no more squares will be revealed.

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        return self.updateBoardDFS(board, click)

    # Time Complexity: O(n * m) where n and m are the rows and columns of board
    # Space Complexity: O(1)
    def updateBoardDFS(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        x, y = click

        if not 0 <= x < rows or not 0 <= y < cols or board[x][y] not in ['E', 'M']:
            return board
        else:
            if board[x][y] == 'M':
                board[x][y] = 'X'
            else:
                adjMines = 0
                for r in range(x - 1, x + 2):
                    for c in range(y - 1, y + 2):
                        if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'M':
                            adjMines += 1

                if adjMines:
                    board[x][y] = str(adjMines)
                else:
                    board[x][y] = 'B'
                    for r in range(x - 1, x + 2):
                        for c in range(y - 1, y + 2):
                            self.updateBoardDFS(board, [r, c])

            return board