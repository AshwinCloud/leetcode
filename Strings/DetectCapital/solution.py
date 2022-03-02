# PROBLEM STATEMENT
# https://leetcode.com/problems/detect-capital/
# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return self.detectCapitalUseRegex(word)

    # Time Complexity: O(n) where n is the size of word
    # Space Complexity: O(1)
    def detectCapitalUseRegex(self, word: str) -> bool:
        import re

        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
