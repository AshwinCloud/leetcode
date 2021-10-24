# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.isAnagramDict(s, t)
    
    def isAnagramSort(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_list = sorted(s)
            t_list = sorted(t)
            
            for i in range(len(s)):
                if s_list[i] != t_list[i]:
                    return False
            return True
    
    def isAnagramDict(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dictionary = {}
            for i in range(len(s)):
                if dictionary.get(s[i]):
                    dictionary[s[i]] += 1
                else:
                    dictionary[s[i]] = 1

                if dictionary.get(t[i]):
                    dictionary[t[i]] -= 1
                else:
                    dictionary[t[i]] = -1
            
            for k, v in dictionary.items():
                if v != 0:
                    return False
            return True