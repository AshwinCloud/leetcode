# PROBLEM STATEMENT
# https://leetcode.com/problems/01-matrix/
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        return self.updateMatrixBFS(mat)

    def updateMatrixBFS(self, mat: List[List[int]]) -> List[List[int]]:
        visited = []

        for row in range(len(mat)):
            for column in range(len(mat[0])):
                if mat[row][column] == 0:
                    visited.insert(0, (row, column))
                else:
                    mat[row][column] = -1

        while visited:
            row, column = visited.pop()

            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                n_row = row + i
                n_column = column + j

                if 0 <= n_row < len(mat) and 0 <= n_column < len(mat[0]) and mat[n_row][n_column] == -1:
                    mat[n_row][n_column] = mat[row][column] + 1
                    visited.insert(0, (n_row, n_column))
        return mat

    def updateMatrixDP(self, mat: List[List[int]]) -> List[List[int]]:
        import sys

        for row in range(len(mat)):
            for column in range(len(mat[0])):
                if mat[row][column] != 0:
                    mat[row][column] = sys.maxsize

        for row in range(len(mat)):
            for column in range(len(mat[0])):
                if row > 0:
                    mat[row][column] = min(mat[row][column], mat[row - 1][column] + 1)
                if column > 0:
                    mat[row][column] = min(mat[row][column], mat[row][column - 1] + 1)

        for row in range(len(mat) - 1, -1, -1):
            for column in range(len(mat[0]) - 1, -1, -1):
                if row < len(mat) - 1:
                    mat[row][column] = min(mat[row][column], mat[row + 1][column] + 1)
                if column < len(mat[0]) - 1:
                    mat[row][column] = min(mat[row][column], mat[row][column + 1] + 1)

        return mat