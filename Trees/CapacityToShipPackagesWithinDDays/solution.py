# PROBLEM STATEMENT
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# A conveyor belt has packages that must be shipped from one port to another within days days.
# The ith package on the conveyor belt has a weight of weights[i].
# Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
# We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        return self.shipWithinDaysBS(weights, days)

    # Time Complexity: O(n * log size) where n is the size of weights and size is the search space (max weight - sum of weights)
    # Space Complexity: O(1)
    def shipWithinDaysBS(self, weights: List[int], days: int) -> int:
        def canShipWithinDays(weights: List[int], days: int, maxWeight: int) -> int:
            numDays = 1
            weightSoFar = 0
            for w in weights:
                if weightSoFar + w > maxWeight:
                    numDays += 1
                    weightSoFar = w
                else:
                    weightSoFar += w

                if numDays > days:
                    return False
            return numDays <= days

        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            print(
                f"low: {low}, high: {high}, mid: {mid}, canShipWithinDays(weights, days, mid): {canShipWithinDays(weights, days, mid)}")

            if canShipWithinDays(weights, days, mid):
                high = mid - 1
            else:
                low = mid + 1

        return low