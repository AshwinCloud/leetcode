# PROBLEM STATEMENT
# https://leetcode.com/problems/implement-trie-prefix-tree/
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
# There are various applications of this data structure, such as autocomplete and spellchecker.
# Implement the Trie class:
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # Time Complexity: O(n) where n is the size of word
    # Space Complexity: O(n) where n is the size of word
    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_word = True

    # Time Complexity: O(n) where n is the size of word
    # Space Complexity: O(1)
    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.is_word

    # Time Complexity: O(n) where n is the size of word
    # Space Complexity: O(1)
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)