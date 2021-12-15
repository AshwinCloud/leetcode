# PROBLEM STATEMENT
# https://leetcode.com/problems/ransom-note/
# Given two stings ransomNote and magazine,
# return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return self.canConstruct1(ransomNote, magazine)

    # Time Complexity: O(n+m) where n is the size of magazine and n is the size of ransomNote
    # Space Complexity: O(1)
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26

        for s in magazine:
            count[ord(s) - ord('a')] += 1

        for s in ransomNote:
            if count[ord(s) - ord('a')] <= 0:
                return False
            else:
                count[ord(s) - ord('a')] -= 1

        return True