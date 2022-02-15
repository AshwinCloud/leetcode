# PROBLEM STATEMENT
# https://leetcode.com/problems/integer-to-english-words/
# Convert a non-negative integer num to its English words representation.
class Solution:
    def numberToWords(self, num: int) -> str:
        return self.numberToWords1(num)

    # Time Complexity: O(n) where n is the number of digits
    # Space Complexity: O(n) where n is the number of digits
    def numberToWords1(self, num: int) -> str:
        zeroToNineteen = "Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split(
            " ")
        twentyToNinety = "Zero Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split(" ")
        bigs = {1000000000: "Billion", 1000000: "Million", 1000: "Thousand", 100: "Hundred"}

        def helper(num: int) -> str:
            answer = []
            if num == 0:
                pass
            elif num < 20:
                answer += [zeroToNineteen[num]]
            elif num < 100:
                answer += [twentyToNinety[num // 10], helper(num % 10)]
            elif num < 1000:
                answer += [zeroToNineteen[num // 100], bigs[100], helper(num % 100)]
            else:
                for i in [1000000000, 1000000, 1000]:
                    if num // i:
                        answer += [self.numberToWords1(num // i), bigs[i]]
                        num %= i
                answer += [helper(num)]

            return ' '.join(answer).strip()

        return helper(num) or 'Zero'