# PROBLEM STATEMENT
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.lengthOfLongestSubstringSlidingWindow(s)
    
    def lengthOfLongestSubstringSlidingWindow(self, s: str) -> int:
        start = 0
        end = 0
        longest_length = 0
        unique_chars = set()
        
        while end < len(s):
            if s[end] not in unique_chars:
                unique_chars.add(s[end])
                longest_length = max(len(unique_chars), longest_length)
                end += 1
            else:
                unique_chars.remove(s[start])
                start += 1
        return longest_length