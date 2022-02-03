# PROBLEM STATEMENT
# https://leetcode.com/problems/non-overlapping-intervals/
# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        return self.eraseOverlapIntervals1(intervals)

    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def eraseOverlapIntervals1(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)

        return res