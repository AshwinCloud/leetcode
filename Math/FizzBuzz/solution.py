# PROBlEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/
# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzBuzzList = []
        
        for i in range(1, n+1):
            fizzBuzz = ""
            fizzBuzz = fizzBuzz + "Fizz" if i % 3 == 0 else fizzBuzz
            fizzBuzz = fizzBuzz + "Buzz" if i % 5 == 0 else fizzBuzz
            fizzBuzz = fizzBuzz or str(i)
            fizzBuzzList.append(fizzBuzz)
        
        return fizzBuzzList