# PROBLEM STATEMENT
# https://leetcode.com/problems/flood-fill/
# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and newColor.
# You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally
# to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally
# to those pixels (also with the same color), and so on.
# Replace the color of all of the aforementioned pixels with newColor.
# Return the modified image after performing the flood fill.
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        return self.floodFillDFS(image, sr, sc, newColor)

    def floodFillDFS(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def helper(image: List[List[int]], sr: int, sc: int, oldColor: int, newColor: int):
            if 0 <= sr < len(image) and 0 <= sc < len(image[0]) and image[sr][sc] == oldColor:
                image[sr][sc] = newColor
                helper(image, sr - 1, sc, oldColor, newColor)
                helper(image, sr + 1, sc, oldColor, newColor)
                helper(image, sr, sc - 1, oldColor, newColor)
                helper(image, sr, sc + 1, oldColor, newColor)

        if image[sr][sc] != newColor:
            helper(image, sr, sc, image[sr][sc], newColor)
        return image