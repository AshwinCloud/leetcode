# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#  countAndSay(1) = "1"
#    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

# To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.
# For example, the saying and conversion for digit string "3322251":
# Given a positive integer n, return the nth term of the count-and-say sequence.

class Solution:
    def countAndSay(self, n: int) -> str:
        return self.countAndSayRecursive(n)

    def countAndSayRecursive(self, n: int) -> str:
        def helper(n: int) -> str:
            if n == 1:
                return "1"
            else:
                say_previous = helper(n-1)
                countAndSay = ""
                i = 0
                while i < len(say_previous):
                    j = 1
                    while i + j < len(say_previous) and say_previous[i] == say_previous[i + j]:
                        j += 1
                    countAndSay += str(j) + say_previous[i]
                    i += j
                return countAndSay
        return helper(n)    