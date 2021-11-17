# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. 
# You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.firstBadVersionIterative(n)

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def firstBadVersionIterative(self, n):
        lower = 0
        upper = n
        firstBadVersion = 0

        while lower <= upper:
            mid = lower + ((upper - lower) // 2)
            is_lower_bad = isBadVersion(lower)
            if is_lower_bad:
                return lower
            else:
                is_mid_bad = isBadVersion(mid)
                if is_mid_bad:
                    firstBadVersion = mid
                    upper = mid - 1
                else:
                    lower = mid + 1

        return firstBadVersion

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def firstBadVersionRecurive(self, n):
        def helper(lower: int, upper: int):
            mid = lower + ((upper - lower) // 2)

            is_lower_bad = isBadVersion(lower)

            if is_lower_bad:
                return lower
            else:
                is_mid_bad = isBadVersion(mid)
                if is_mid_bad:
                    return helper(lower, mid - 1)
                else:
                    return helper(mid + 1, upper)

        return helper(0, n)