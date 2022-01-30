# PROBLEM STATEMENT
# https://leetcode.com/problems/spiral-matrix/
# Given an m x n matrix, return all elements of the matrix in spiral order.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.spiralOrder1(matrix)

    # Time Complexity: O(m * n) where m and n are the rows and columns of matrix
    # Space Complexity: O(m * n) including the storage for the output and O(m * n) including the storage for the output
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        l = []
        reverseOrder = False
        while left <= right and top <= bottom:
            if not reverseOrder:
                for c in range(left, right + 1):
                    l.append(matrix[top][c])
                top += 1

                for r in range(top, bottom + 1):
                    l.append(matrix[r][right])
                right -= 1
            else:
                for c in range(right, left - 1, -1):
                    l.append(matrix[bottom][c])
                bottom -= 1

                for r in range(bottom, top - 1, -1):
                    l.append(matrix[r][left])
                left += 1

            reverseOrder = not reverseOrder

        return l