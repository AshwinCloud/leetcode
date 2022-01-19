# PROBLEM STATEMENT
# https://leetcode.com/problems/word-search-ii/
# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    # Time Complexity: O(w) where w is the size of the word
    # Space Complexity: O(w)
    def addWord(self, word: str) -> None:
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_word = True


class Solution:

    # Time Complexity: O((n * w) + (r * c * 4^w)) where n is the number of words, w is the average size of each word, r and c are the number of rows and columns in the board
    #                  O(n * w) for populating Trie and O(r * c * 4^w) for traversing through the board
    # Space Complexity: O((n * w) + (r * c))
    #                   O(n * w) for Trie, O(n * w) for result and O(r * c) for travering the board (visited)
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(board: List[List[str]], word: str, board_row: int, board_col: int, trienode: TrieNode,
                visited: List[List[bool]], result: Set[str]) -> None:
            if (board_row < 0
                    or board_row >= len(board)
                    or board_col < 0
                    or board_col >= len(board[0])
                    or visited[board_row][board_col]
                    or board[board_row][board_col] not in trienode.children.keys()):
                return
            else:
                visited[board_row][board_col] = True

                word += board[board_row][board_col]
                node = trienode.children[board[board_row][board_col]]
                if node.is_word:
                    result.add(word)

                if len(node.children.keys()) != 0:
                    for (i, j) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                        dfs(board, word, board_row + i, board_col + j, node, visited, result)

                visited[board_row][board_col] = False

        wordsTrie = TrieNode()
        for word in words:
            wordsTrie.addWord(word)

        rows = len(board)
        cols = len(board[0])
        result = set()
        visited = [[False] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                dfs(board, "", r, c, wordsTrie, visited, result)

        return list(result)