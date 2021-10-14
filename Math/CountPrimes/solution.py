# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/
# Given an integer n, return the number of prime numbers that are strictly less than n.
class Solution:
    def countPrimes(self, n: int) -> int:
        return self.countPrimesSieveOfEratosthenes(n)
    
    def countPrimesSieveOfEratosthenes(self, n: int) -> int:
            if n <= 1:
                return 0
            else:
                list_num_is_prime = [True] * (n)
                list_num_is_prime[0] = False
                list_num_is_prime[1] = False

                for i in range(2, round(sqrt(n))+1):
                    if list_num_is_prime[i]:
                        for j in range(i*i, n, i):
                            list_num_is_prime[j] = False
                total = list_num_is_prime.count(True)
                return total