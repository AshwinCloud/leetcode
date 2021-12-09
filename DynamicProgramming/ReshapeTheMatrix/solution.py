# PROBLEM STATEMENT
# https://leetcode.com/problems/reshape-the-matrix/
# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix
# into a new one with a different size r x c keeping its original data.
# You are given an m x n matrix mat and two integers r and c representing
# the number of rows and the number of columns of the wanted reshaped matrix.
# The reshaped matrix should be filled with all the elements of the
# original matrix in the same row-traversing order as they were.
# If the reshape operation with given parameters is possible and legal,
# output the new reshaped matrix; Otherwise, output the original matrix.
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        return self.matrixReshapeDP1(mat, r, c)

    # Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in mat
    # Space Complexity: O(m * n) where m is the number of rows and n is the number of columns in mat
    def matrixReshapeDP1(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        orig_r = len(mat)
        orig_c = len(mat[0])

        if orig_r * orig_c != r * c:
            return mat
        else:
            new_mat = []
            new_row = []
            new_i = new_j = 0

            for row in mat:
                for val in row:
                    new_row.append(val)

                    if len(new_row) == c:
                        new_mat.append(new_row)
                        new_row = []

            return new_mat

    # Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in mat
    # Space Complexity: O(m * n) where m is the number of rows and n is the number of columns in mat
    def matrixReshapeDP2(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        orig_r = len(mat)
        orig_c = len(mat[0])

        if orig_r * orig_c != r * c:
            return mat
        else:
            new_mat = [[None for i in range(c)] for j in range(r)]
            new_i = new_j = 0

            for orig_i in range(orig_r):
                for orig_j in range(orig_c):
                    new_mat[new_i][new_j] = mat[orig_i][orig_j]

                    if new_j < c - 1:
                        new_j += 1
                    else:
                        new_i += 1
                        new_j = 0
            return new_mat