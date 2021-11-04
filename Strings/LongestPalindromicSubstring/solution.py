# PROBLEM STATEMENT
# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.longestPalindromeExpand(s)

    # Time Complexity: O(n^2)
    # Space Complexity: 1
    def longestPalindromeExpandAroundCenter(self, s: str) -> str:
        def expandAroundCenter(s: str, left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        global_max_len = 0
        center = 0
        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)
            local_max_len = max(len1, len2)

            if local_max_len > global_max_len:
                global_max_len = local_max_len
                center = i

        start = center - (global_max_len - 1) // 2
        end = start + global_max_len

        return s[start:end]