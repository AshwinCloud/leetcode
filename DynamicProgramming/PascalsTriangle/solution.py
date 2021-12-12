# PROBLEM STATEMENT
# https://leetcode.com/problems/pascals-triangle/
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return self.generateDP(numRows)

    # Time Complexity: O(n) where n is the number of rows
    # Space Complexity: O(1) when not including space for result, O(n^2) when including space for result
    # Summation: (n * (n+1)) / 2 ~ O(n^2)
    def generateDP(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        else:
            triangle = [[1]]

            for i in range(1, numRows):
                prev_row = triangle[i - 1]
                row = [1]

                for j in range(1, i):
                    row.append(prev_row[j - 1] + prev_row[j])

                row.append(1)
                triangle.append(row)
            return triangle