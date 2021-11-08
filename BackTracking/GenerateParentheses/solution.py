# PROBLEM STATEMENT
# https://leetcode.com/problems/generate-parentheses/
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generageParenthesisBacktrack(n)

    def generageParenthesisBacktrack(self, n: int) -> List[str]:
        def backtrack(max_num: int, open_num: int, close_num: max, list_str: list[str], current_str: str):
            if len(current_str) == max_num * 2:
                list_str.append(current_str)

            if open_num < max_num:
                backtrack(max_num, open_num + 1, close_num, list_str, current_str + '(')

            if close_num < open_num:
                backtrack(max_num, open_num, close_num + 1, list_str, current_str + ')')

        list_str = []
        backtrack(n, 0, 0, list_str, '')
        return list_str