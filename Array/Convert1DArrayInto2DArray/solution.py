# 2022. Convert 1D Array Into 2D Array
# PROBLEM STATEMENT
# https://leetcode.com/problems/convert-1d-array-into-2d-array/
# You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n.
# You are tasked with creating a 2-dimensional (2D) array with m rows and n columns using all the elements from original.
# The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array,
# the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.
# Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return self.construct2DArray2(original, m, n)

    # TIME COMPLEXITY: O(m * n)
    # SPACE COMPLEXITY: O(m * n) and O(1) with and without including the space for result
    def construct2DArray1(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        else:
            result = [[0] * n for _ in range(m)]

            row = col = 0
            for i in range(len(original)):
                result[row][col] = original[i]
                if col == n - 1:
                    col = 0
                    row += 1
                else:
                    col += 1

            return result

    # TIME COMPLEXITY: O(m * n)
    # SPACE COMPLEXITY: O(m * n) and O(1) with and without including the space for result
    def construct2DArray2(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []

        if len(original) == m * n:
            for i in range(0, len(original), n):
                print(f"i: {i}")
                result.append(original[i:i + n])
        return result