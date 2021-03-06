# PROBLEM STATEMENT
# https://leetcode.com/problems/find-the-difference/
# You are given two strings s and t.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Return the letter that was added to t.
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return self.findTheDifferenceArray(s, t)

    # Time Complexity: O(n) where s is the size of s
    # Space Complexity: O(1)
    def findTheDifferenceArray(self, s: str, t: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            if count[ord(ch) - ord('a')] == 0:
                return ch
            else:
                count[ord(ch) - ord('a')] -= 1

        return ""