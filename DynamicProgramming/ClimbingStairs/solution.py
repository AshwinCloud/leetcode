# PROBLEM STATEMENT
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbStairsMemoizationIterative(n)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def climbStairsMemoizationRecursive(self, n: int) -> int:
        def helper(n, memory) -> int:
            if memory.get(n):
                return memory[n]
            else:
                memory[n] = helper(n - 2, memory) + helper(n - 1, memory)
                return memory[n]

        memory = {0: 0, 1: 1, 2: 2}
        return helper(n, memory)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def climbStairsMemoizationIterative(self, n: int) -> int:
        memory = {0: 0, 1: 1, 2: 2}

        for i in range(3, n + 1):
            memory[i] = memory[i - 1] + memory[i - 2]

        return memory[n]