# PROBLEM STATEMENT
# https://leetcode.com/problems/decode-ways/
# A message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
# Given a string s containing only digits, return the number of ways to decode it.
# The test cases are generated so that the answer fits in a 32-bit integer.
class Solution:
    def numDecodings(self, s: str) -> int:
        return self.numDecodingsDFS(s)

    # Recursive Top Down Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def numDecodingsDFS(self, s: str) -> int:
        def helper(i: int, dp={len(s): 1}) -> int:
            if i in dp:
                return dp[i]
            elif s[i] == "0":
                return 0
            else:
                res = helper(i + 1)

                if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and 0 <= int(s[i + 1]) <= 6)):
                    res += helper(i + 2, dp)

                dp[i] = res

                return dp[i]

        return helper(0)

    # Iterative Bottom Up Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def numDecodingsDP(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        else:
            prev_prev_dp = 1  # len(s)
            prev_dp = 0 if s[len(s) - 1] == "0" else 1  # len(s) - 1

            for i in range(len(s) - 2, -1, -1):
                dp = 0 if s[i] == "0" else prev_dp

                if s[i] == "1" or (s[i] == "2" and 0 <= int(s[i + 1]) <= 6):
                    dp += prev_prev_dp

                prev_prev_dp, prev_dp = prev_dp, dp

            return prev_dp