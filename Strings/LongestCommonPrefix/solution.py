# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.longestCommonPrefixSort(strs)
    
    def longestCommonPrefixWithoutSort(self, strs: List[str]) -> str:
        common_prefix = ""
        first_str = strs[0]
        for i in range(len(first_str)):
            for s in strs:
                if len(s) <= i or first_str[i] != s[i]:
                    return common_prefix
            common_prefix += first_str[i]
        return common_prefix
    
    def longestCommonPrefixSort(self, strs: List[str]) -> str:
        strs.sort()
        common_prefix_index = -1
        for i in range(len(strs[0])):
            if len(strs[len(strs)-1]) <= i or strs[0][i] != strs[len(strs)-1][i]:
                break
            common_prefix_index = i
            
        return "" if common_prefix_index == -1 else strs[0][:common_prefix_index+1]