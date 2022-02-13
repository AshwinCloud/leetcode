# PROBLEM STATEMENT
# https://leetcode.com/problems/concatenated-words/
# Given an array of strings words (without duplicates),
# return all the concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of
# at least two shorter words in the given array.
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        return self.findAllConcatenatedWordsInADictDFS(words)

    # Time Complexity: O(n^2 * m) where m is the size of words and n is the size of the largest word
    # Space Complexity: O(n^2 * m)
    def findAllConcatenatedWordsInADictDFS(self, words: List[str]) -> List[str]:
        wordsSet = set(words)
        concatinatedWordsInDict = list()  # only the ones in words
        memo = dict()  # all the words including the ones not in words

        def isConcatinatedWord(word: str, index: int) -> bool:
            if not word:
                return False
            elif index > 0 and word[index:] in wordsSet:
                return True
            elif word[index:] in memo:
                return memo[word[index:]]
            else:
                memo[word] = False
                for i in range(index + 1, len(word)):
                    if word[index:i] in wordsSet and isConcatinatedWord(word, i):
                        memo[word] = True
                        break
                return memo[word]

        for word in words:
            if isConcatinatedWord(word, 0):
                concatinatedWordsInDict.append(word)

        return concatinatedWordsInDict