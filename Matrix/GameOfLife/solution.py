# PROBLEM STATEMENT
# https://leetcode.com/problems/game-of-life/
# According to Wikipedia's article: "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
# The board is made up of an m x n grid of cells, where each cell has an initial state: live
# (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors
# (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state,
# where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.gameOfLife1(board)

    # Time Complexity: O(n * m) where n and m are the rows and columns of board
    # Space Complexity: O(1)
    def gameOfLife1(self, board: List[List[int]]) -> None:

        # Time Complexity: O(3 * 3)
        # Space Complexity: O(1)
        def numLiveNeighbors(board: List[List[int]], row: int, col: int) -> int:
            liveNeighbors = 0
            rows, cols = len(board), len(board[0])
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if (not (r == row and c == col) and
                            0 <= r < rows and
                            0 <= c < cols):
                        liveNeighbors += 1 if board[r][c] in [1, 3] else 0

            return liveNeighbors

        rows, cols = len(board), len(board[0])

        #   OLD     |   NEW     |   Val
        #   0       |   0       |   0
        #   0       |   1       |   2
        #   1       |   0       |   3
        #   1       |   1       |   1

        for r in range(rows):
            for c in range(cols):
                liveNeighbors = numLiveNeighbors(board, r, c)

                if board[r][c]:
                    if liveNeighbors < 2:
                        board[r][c] = 3
                    elif liveNeighbors <= 3:
                        board[r][c] = 1
                    else:
                        board[r][c] = 3
                else:
                    if liveNeighbors == 3:
                        board[r][c] = 2
                    else:
                        board[r][c] = 0

        for r in range(rows):
            for c in range(cols):
                board[r][c] = 0 if board[r][c] in [0, 3] else 1

        return None