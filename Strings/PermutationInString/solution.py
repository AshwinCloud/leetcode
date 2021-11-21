# PROBLEM STATEMENT
# https://leetcode.com/problems/permutation-in-string/
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.checkInclusionSlidingWindowArraysOptimized(s1, s2)

    def checkInclusionSlidingWindowArrays(self, s1: str, s2: str) -> bool:
        def matches(list_s1: List[int], list_s2: List[int]) -> bool:
            for i in range(0, len(list_s1)):
                if list_s1[i] != list_s2[i]:
                    return False
            return True

        if len(s1) > len(s2):
            return False

        else:
            list_s1 = [0] * 26
            list_s2 = [0] * 26

            for i in range(0, len(s1)):
                list_s1[97 - ord(s1[i])] += 1
                list_s2[97 - ord(s2[i])] += 1

            if matches(list_s1, list_s2):
                return True

            for i in range(len(s1), len(s2)):
                list_s2[97 - ord(s2[i - len(s1)])] -= 1
                list_s2[97 - ord(s2[i])] += 1

                if matches(list_s1, list_s2):
                    return True

            return False

    def checkInclusionSlidingWindowDicts(self, s1: str, s2: str) -> bool:

        def matches(dict_s1, dict_s2) -> bool:
            if len(dict_s1.keys()) != len(dict_s2.keys()):
                return False

            for key, value in dict_s1.items():
                if not dict_s2.get(key) or dict_s2[key] != dict_s1[key]:
                    return False
            return True

        if len(s1) > len(s2):
            return False

        else:
            dict_s1 = {}
            dict_s2 = {}

            for i in range(0, len(s1)):
                dict_s1[97 - ord(s1[i])] = dict_s1.get(97 - ord(s1[i]), 0) + 1
                dict_s2[97 - ord(s2[i])] = dict_s2.get(97 - ord(s2[i]), 0) + 1

            if matches(dict_s1, dict_s2):
                return True

            for i in range(len(s1), len(s2)):
                if dict_s2[97 - ord(s2[i - len(s1)])] == 1:
                    dict_s2.pop(97 - ord(s2[i - len(s1)]))
                else:
                    dict_s2[97 - ord(s2[i - len(s1)])] -= 1

                dict_s2[97 - ord(s2[i])] = dict_s2.get(97 - ord(s2[i]), 0) + 1

                if matches(dict_s1, dict_s2):
                    return True

            return False