# PROBLEM STATEMENT
# https://leetcode.com/problems/length-of-last-word/
# Given a string s consisting of some words separated by some number of spaces,
# return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return self.lengthOfLastWord1(s)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lengthOfLastWord1(self, s: str) -> int:
        last_non_space = len(s) - 1
        while s[last_non_space].isspace():
            last_non_space -= 1

        curr_length = 0
        for i in range(last_non_space + 1):
            if s[i].isspace():
                curr_length = 0
            else:
                curr_length += 1

        return curr_length