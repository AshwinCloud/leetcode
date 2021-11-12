# PROBLEM STATEMENT
# https://leetcode.com/problems/valid-sudoku/
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidSudokuSingleSet(board)

    def isValidSudokuSingleSet(self, board: List[List[str]]) -> bool:
        seen_set = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    row_str = str(board[i][j]) + " - row - " + str(i)
                    col_str = str(board[i][j]) + " - col - " + str(j)
                    box_str = str(board[i][j]) + " - box - " + str(i // 3) + "," + str(j // 3)

                    if row_str in seen_set or col_str in seen_set or box_str in seen_set:
                        return False
                    else:
                        seen_set.add(row_str)
                        seen_set.add(col_str)
                        seen_set.add(box_str)
        return True