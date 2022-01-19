# PROBLEM STATEMENT
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Implement the WordDictionary class:
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
# word may contain dots '.' where dots can be matched with any letter.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    # Time Complexity: O(h) where h is the height of the Trie, at most h == n, so O(n)
    # Space Complexity: O(n) where n is the number of characters in the word
    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_word = True

    # Time Complexity: O(n) involving '.' and O(h) without involving '.' and at most h == n, so O(n)
    # Space Complexity: O(1)
    def search(self, word: str) -> bool:
        def dfs(children, word: str, word_index: int) -> bool:
            c = word[word_index]

            if c == '.':
                if len(children) == 0:
                    return False
                elif word_index == len(word) - 1:
                    for child in children.values():
                        if child.is_word:
                            return True
                    return False
                else:
                    for child in children.values():
                        if dfs(child.children, word, word_index + 1):
                            return True
                    return False
            else:
                if c not in children:
                    return False
                elif word_index == len(word) - 1:
                    return children[c].is_word
                else:
                    return dfs(children[c].children, word, word_index + 1)

            return False

        return dfs(self.root.children, word, 0)

        # Time Complexity: O(n) involving '.' and O(h) without involving '.' and at most h == n, so O(n)
        # Space Complexity: O(1)
        def search2(self, word: str) -> bool:
            def dfs(startIndex: int, word: str, root: TrieNode) -> bool:
                current = root

                for i in range(startIndex, len(word)):
                    c = word[i]

                    if c == '.':
                        for child in current.children.values():
                            if dfs(i + 1, word, child):
                                return True
                        return False
                    else:
                        if c in current.children:
                            current = current.children[c]
                        else:
                            return False
                return current.word

            return dfs(0, word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)