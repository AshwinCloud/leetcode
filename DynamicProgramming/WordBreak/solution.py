# PROBLEM STATEMENT
# https://leetcode.com/problems/word-break/
# Given a string s and a dictionary of strings wordDict,
# return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.wordBreakDP(s, wordDict)

    # Time Complexity: O(n * m * n) where n is the size of s and m is the size or wordDict
    # Space Complexity: O(n) where n is the size of s
    def wordBreakDP(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]

                if dp[i] == True:
                    break

        return dp[0]