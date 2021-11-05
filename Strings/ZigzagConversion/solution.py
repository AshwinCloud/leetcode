# PROBLEM STATEMENT
# https://leetcode.com/problems/zigzag-conversion/
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return self.convertNStrings(s, numRows)

    def convertNStrings(self, s: str, numRows: int) -> str:
        if not s or numRows == 1:
            return s
        else:
            n_strings = numRows * [""]
            row = step = 0
            for i in range(len(s)):
                n_strings[row] += s[i]

                if row == 0:
                    step = 1
                if row == numRows - 1:
                    step = -1

                row += step

            result = ""
            for string in n_strings:
                result += string

            return result