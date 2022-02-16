# PROBLEM STATEMENT
# https://leetcode.com/problems/most-common-word/
# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned.
# It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return self.mostCommonWordOnePass(paragraph, banned)

    # Time Complexity: O(n + m) where n and m are the sizes of paragraph and banned
    # Space Complexity: O(n + w) worst case where each word in paragraph is unique
    def mostCommonWordOnePass(self, paragraph: str, banned: List[str]) -> str:
        from collections import defaultdict
        banned = set(banned)
        wordCount = defaultdict(lambda: 0)
        mostCommonWord = ""
        currentWordBuffer = []
        lengthParagraph = len(paragraph)

        for i, ch in enumerate(paragraph):
            if ch.isalnum():
                currentWordBuffer.append(ch.lower())

            if not ch.isalnum() or i == lengthParagraph - 1:
                currentWord = ''.join(currentWordBuffer)

                if currentWord and currentWord not in banned:
                    wordCount[currentWord] += 1
                    mostCommonWord = mostCommonWord if wordCount[mostCommonWord] > wordCount[
                        currentWord] else currentWord
                currentWordBuffer = []

        return mostCommonWord