# PROBLEM STATEMENT
# https://leetcode.com/problems/intersection-of-two-arrays/
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.intersectionSort(nums1, nums2)

    # Time Complexity: O(n + m) where n is the size of the larger list between nums1 and nums2
    # Space Complexity: O(n + m) where n and m are the sizes of nums1 and nums2
    def intersectionSet(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1) if len(nums1) < len(nums2) else set(nums2)
        list2 = nums2 if len(nums1) < len(nums2) else nums1
        resultSet = set()

        for l in list2:
            if l in set1:
                resultSet.add(l)

        return list(resultSet)

    # Time Complexity: O(n log n + m log m) where n and m are the sizes of nums1 and nums2
    #                  ~ O(n log n) where n is the size of the larger list between nums1 and nums 2
    # Space Complexity: O(1) and O(n) with and without including the space for result
    def intersectionSort(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []

        len1 = len(nums1)
        len2 = len(nums2)
        l1 = l2 = 0

        while l1 < len1 and l2 < len2:
            left, right = nums1[l1], nums2[l2]

            if left > right:
                l2 += 1
            elif left < right:
                l1 += 1
            else:
                result.append(nums1[l1])

                while l1 < len1 and left == nums1[l1]:
                    l1 += 1

                while l2 < len2 and right == nums2[l2]:
                    l2 += 1
        return result