# PROBLEM STATEMENT
# https://leetcode.com/problems/group-anagrams/
# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.groupAnagramsDict(strs)

    # Time Complexity: O(m * n) where m is the size of strs and n is the average length of each string in strs
    # Space Complexity: O(m) without including the result and O(m * n) with including the result
    def groupAnagramsDict(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            result[tuple(count)].append(s)

        return result.values()
