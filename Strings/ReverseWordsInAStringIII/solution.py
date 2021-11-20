# PROBLEM STATEMENT
# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Given a string s, reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.
class Solution:
    def reverseWords(self, s: str) -> str:
        return self.reverseWordsTwoPointers(s)

    def reverseWordsTwoPointers(self, s: str) -> str:
        def reverse(s: str, left: int, right: int) -> str:
            new_string = ""
            while left <= right:
                new_string += s[right]
                right -= 1
            return new_string

        def concat_strings(s1: str, s2: str) -> str:
            if s1:
                s1 += " "
            s1 += s2
            return s1

        left = 0
        right = 0
        new_sentence = ""

        while left <= right < len(s):
            if s[right] != ' ':
                right += 1
            else:
                new_sentence = concat_strings(new_sentence, reverse(s, left, right - 1))
                right += 1
                left = right

        new_sentence = concat_strings(new_sentence, reverse(s, left, right - 1))

        return new_sentence