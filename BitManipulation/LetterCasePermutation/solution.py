# PROBLEM STATEMENT
# https://leetcode.com/problems/letter-case-permutation/
# Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. You can return the output in any order.
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        return self.letterCasePermutationBitwise(s)

    # Time Complexity: O(2^n) where n is the number of alpha characters in string s
    # Space Complexity: O(2^n) where n is the number of alpha characters in string s
    def letterCasePermutationDFS(self, s: str) -> List[str]:

        def dfs(s: str, partial_s: str = "", index: int = 0, result: List[str] = []) -> List[str]:
            if len(partial_s) == len(s):
                result.append(partial_s)
            else:
                dfs(s, partial_s + s[index], index + 1, result)

                if s[index].isalpha():
                    dfs(s, partial_s + s[index].upper(), index + 1, result)

            return result

        return dfs(s.lower())

    # Time Complexity: O(2^n) where n is the number of alpha characters in string s
    # Space Complexity: O(2^n) where n is the number of alpha characters in string s
    def letterCasePermutationBitwise(self, s: str) -> List[str]:
        num_alpha = 0
        for i in range(len(s)):
            if s[i].isalpha():
                num_alpha += 1

        num_perms = 1 << num_alpha
        result = []

        for count_perm in range(num_perms):
            perm = ""
            count_alpha = 0
            for count_s in range(len(s)):
                if s[count_s].isalpha():
                    if (count_perm >> count_alpha) & 1 == 1:
                        perm += s[count_s].upper()
                    else:
                        perm += s[count_s].lower()
                    count_alpha += 1
                else:
                    perm += s[count_s]
            result.append(perm)

        return result