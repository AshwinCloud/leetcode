# PROBLEM STATEMENT
# https://leetcode.com/problems/container-with-most-water/
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Notice that you may not slant the container.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        return self.maxAreaOnePass(height)

    def maxAreaBruteForce(self, height: List[int]) -> int:
        max_area = 0

        for i in range(len(height)):
            for j in range(i, len(height)):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)

        return max_area

    def maxAreaOnePass(self, height: List[int]) -> int:
        max_area = 0
        start_pointer = 0
        end_pointer = len(height) - 1

        while start_pointer < end_pointer:
            area = min(height[start_pointer], height[end_pointer]) * (end_pointer - start_pointer)
            max_area = max(max_area, area)

            if height[start_pointer] < height[end_pointer]:
                start_pointer += 1
            else:
                end_pointer -= 1

        return max_area