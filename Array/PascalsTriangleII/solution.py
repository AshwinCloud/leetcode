# PROBLEM STATEMENT
# https://leetcode.com/problems/pascals-triangle-ii/
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return self.getRowDP(rowIndex)

    # Time Complexity: O(n) where n is the rowIndex
    # Space Complexity: O(n) including the space for result
    def getRowDP(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            row = [1] * (rowIndex + 1)
            num_col = 2

            for i in range(1, rowIndex):
                for j in range(num_col - 1, 0, -1):
                    row[j] += row[j - 1]
                num_col += 1
            return row