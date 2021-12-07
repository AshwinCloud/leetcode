# PROBLEM STATEMENT
# https://leetcode.com/problems/search-a-2d-matrix/
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.searchMatrixBin(matrix, target)

    # Time Complexity: O(log m + log n) where m is the number of rows and n is the number of columns
    def searchMatrixBin(self, matrix: List[List[int]], target: int) -> bool:
        first_row, last_row = 0, len(matrix) - 1

        while first_row <= last_row:
            mid_row = (first_row + last_row) // 2
            if target < matrix[mid_row][0]:
                last_row = mid_row - 1
            elif target > matrix[mid_row][-1]:
                first_row = mid_row + 1
            else:
                break

        if first_row > last_row:
            return False

        first_col, last_col = 0, len(matrix[mid_row])

        while first_col <= last_col:
            mid_col = (first_col + last_col) // 2
            if target < matrix[mid_row][mid_col]:
                last_col = mid_col - 1
            elif target > matrix[mid_row][mid_col]:
                first_col = mid_col + 1
            else:
                return True

        return False


