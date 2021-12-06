# PROBLEM STATEMENT
# https://leetcode.com/problems/min-cost-climbing-stairs/
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.minCostClimbingStairsDPTopDown(cost)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minCostClimbingStairsDPBottomUp(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        else:
            min_cost_1 = cost[0]
            min_cost_2 = cost[1]

            for i in range(2, len(cost)):
                min_cost_1, min_cost_2 = min_cost_2, min(min_cost_1, min_cost_2) + cost[i]

            return min(min_cost_1, min_cost_2)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minCostClimbingStairsDPTopDown(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        else:

            min_cost_1 = cost[len(cost) - 1]
            min_cost_2 = cost[len(cost) - 2]

            for i in range(len(cost) - 3, -1, -1):
                min_cost_1, min_cost_2 = min_cost_2, min(min_cost_1, min_cost_2) + cost[i]

            return min(min_cost_1, min_cost_2)