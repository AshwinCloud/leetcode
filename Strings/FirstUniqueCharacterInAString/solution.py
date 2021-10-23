# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return self.firstUniqCharDict(s)
    
    def firstUniqCharDict(self, s: str) -> int:
        from collections import OrderedDict
        dictionary = OrderedDict()
        
        for i in range(len(s)):
            if dictionary.get(s[i]):
                dictionary[s[i]] = (dictionary[s[i]][0], dictionary[s[i]][1]+1)
            else:
                dictionary[s[i]] = (i, 1)
        
        for k, v in dictionary.items():
            if v[1] == 1:
                return v[0]
        
        return -1