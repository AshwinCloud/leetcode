# PROBLEM STATEMENT
# https://leetcode.com/problems/find-median-from-data-stream/submissions/
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def addNum(self, num: int) -> None:
        import heapq

        heapq.heappush(self.maxheap, -1 * num)

        if self.minheap and self.maxheap and self.minheap[0] < -1 * self.maxheap[0]:
            pop = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, pop)

        if len(self.maxheap) > len(self.minheap) + 1:
            pop = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, pop)
        elif len(self.maxheap) + 1 < len(self.minheap):
            pop = -1 * heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, pop)

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def findMedian(self) -> float:
        if not self.minheap and not self.maxheap:
            return 0
        elif len(self.minheap) < len(self.maxheap):
            return -1 * self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return (self.minheap[0] + (-1 * self.maxheap[0])) / 2

    # Your MedianFinder object will be instantiated and called as such:
    # obj = MedianFinder()
    # obj.addNum(num)
    # param_2 = obj.findMedian()