# You are given an integer array values where values[i] represents the value of the ith sightseeing spot.
# Two sightseeing spots i and j have a distance j - i between them.
# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j:
# the sum of the values of the sightseeing spots, minus the distance between them.
# Return the maximum score of a pair of sightseeing spots.
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        return self.maxScoreSightseeingPairDP(values)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxScoreSightseeingPairDP(self, values: List[int]) -> int:
        import sys
        max_ai = max_score = -1 * sys.maxsize

        for v_ind in range(1, len(values)):
            max_ai = max(max_ai, values[v_ind - 1] + v_ind - 1)
            aj = values[v_ind] - v_ind
            max_score = max(max_score, max_ai + aj)

        return max_score