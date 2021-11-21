# PROBLEM STATEMENT
# https://leetcode.com/problems/permutation-in-string/
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.checkInclusionSlidingWindowArraysOptimized(s1, s2)

    # Time complexity: O(l1 + (l2 - l1)),
    # where l1 is the length of string s1 and l2 is the length of string s2
    # Space complexity: O(1)
    def checkInclusionSlidingWindowArraysOptimized(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            list_s1 = [0] * 26
            list_s2 = [0] * 26

            for i in range(0, len(s1)):
                list_s1[ord(s1[i]) - ord('a')] += 1
                list_s2[ord(s2[i]) - ord('a')] += 1

            match_count = 0

            for i in range(0, len(list_s1)):
                if list_s1[i] == list_s2[i]:
                    match_count += 1

            if match_count == 26:
                return True

            for i in range(len(s1), len(s2)):
                end_index = ord(s2[i]) - ord('a')
                start_index = ord(s2[i - len(s1)]) - ord('a')

                list_s2[end_index] += 1

                if list_s1[end_index] == list_s2[end_index]:
                    match_count += 1
                elif list_s1[end_index] == list_s2[end_index] - 1:
                    match_count -= 1

                list_s2[start_index] -= 1

                if list_s1[start_index] == list_s2[start_index]:
                    match_count += 1
                elif list_s1[start_index] == list_s2[start_index] + 1:
                    match_count -= 1

                if match_count == 26:
                    return True

            return False

    # Time complexity: O(l1 + 26*(l2 - l1)),
    # where l1 is the length of string s1 and l2 is the length of string s2
    # Space complexity: O(1)
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
                list_s1[ord(s1[i]) - ord('a')] += 1
                list_s2[ord(s2[i]) - ord('a')] += 1

            if matches(list_s1, list_s2):
                return True

            for i in range(len(s1), len(s2)):
                list_s2[ord(s2[i - len(s1)]) - ord('a')] -= 1
                list_s2[ord(s2[i]) - ord('a')] += 1

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
                dict_s1[ord(s1[i]) - ord('a')] = dict_s1.get(ord(s1[i]) - ord('a'), 0) + 1
                dict_s2[ord(s2[i]) - ord('a')] = dict_s2.get(ord(s2[i]) - ord('a'), 0) + 1

            if matches(dict_s1, dict_s2):
                return True

            for i in range(len(s1), len(s2)):
                if dict_s2[ord(s2[i - len(s1)]) - ord('a')] == 1:
                    dict_s2.pop(ord(s2[i - len(s1)]) - ord('a'))
                else:
                    dict_s2[ord(s2[i - len(s1)]) - ord('a')] -= 1

                dict_s2[ord(s2[i]) - ord('a')] = dict_s2.get(ord(s2[i]) - ord('a'), 0) + 1

                if matches(dict_s1, dict_s2):
                    return True

            return False