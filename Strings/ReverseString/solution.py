# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
# Write a function that reverses a string. The input string is given as an array of characters s.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return self.reverseStringInPlace(s)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseStringInPlace(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1