# PROBLEM STATEMENT
# https://leetcode.com/problems/set-matrix-zeroes/
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
# You must do it in place.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        return self.setZeroesInPlace(matrix)

    # Time Complexity: O(m * n) where m and n are the rows and cols in matrix
    # Space Complexity: O(1)
    def setZeroesInPlace(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row0 = col0 = matrix[0][0]

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        row0 = 0
                    else:
                        matrix[r][0] = 0

                    if c == 0:
                        col0 = 0
                    else:
                        matrix[0][c] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if row0 == 0:
            for c in range(cols):
                matrix[0][c] = 0

        if col0 == 0:
            for r in range(rows):
                matrix[r][0] = 0