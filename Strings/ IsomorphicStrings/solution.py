# PROBLEM STATEMENT
# https://leetcode.com/problems/isomorphic-strings/
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.isIsomorphicIterative(s, t)

    # Time Complexity: O(n) where n is the size of s and t
    # Space Complexity: O(1)
    def isIsomorphicIterative(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            char_dict_s_to_t = {}
            char_dict_t_to_s = {}

            for i in range(len(s)):
                if s[i] not in char_dict_s_to_t:
                    char_dict_s_to_t[s[i]] = t[i]

                if t[i] not in char_dict_t_to_s:
                    char_dict_t_to_s[t[i]] = s[i]

                if char_dict_s_to_t[s[i]] != t[i]:
                    return False

                if char_dict_t_to_s[t[i]] != s[i]:
                    return False

            return True