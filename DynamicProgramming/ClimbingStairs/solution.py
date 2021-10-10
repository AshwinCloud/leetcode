# PROBLEM STATEMENT
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbStairsMemoizationIterative(n)
    
    def climbStairsMemoizationRecursive(self, n: int) -> int:
        def helper(n: int, memory) -> int:
            if memory.get(n):
                return memory[n]
            else:
                if n <= 2:
                    memory = {0:0, 1:1, 2:2}
                else:                    
                    memory[n] = helper(n-1, memory) + helper(n-2, memory)
                return memory[n]
        return helper(n, {})
    
    def climbStairsMemoizationIterative(self, n: int) -> int:
        memory = {0:0, 1:1, 2:2}
        
        i = 3
        while i <= n:
            memory[i] = memory[i-1] + memory[i-2]
            i += 1

        return memory[n]