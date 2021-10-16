# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        self.mergeSortedArray(nums1, m, nums2, n)
        
    def mergeSortedArray(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx = m + n - 1
        i = m - 1
        j = n - 1
        while idx >= 0: 
            if i >= 0 and j >= 0:
                if nums1[i] > nums2[j]:
                    nums1[idx] = nums1[i]
                    i -= 1
                else:
                    nums1[idx] = nums2[j]
                    j -= 1
            elif i >= 0:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1