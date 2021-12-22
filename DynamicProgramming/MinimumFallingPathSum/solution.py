class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        return self.minFallingPathSumDPInPlace(matrix)

    # Time Complexity: O(n * m)
    # Space Complexity: O(1) in place by mutating the input
    # Top Bottom Approach
    # REFERENCE: https://leetcode.com/problems/minimum-falling-path-sum/discuss/1634409/Top-down-and-bottom-up-DP-solutions-in-Python
    def minFallingPathSumDPInPlace(self, matrix: List[List[int]]) -> int:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        import math
        for r in range(1, n_rows):
            for c in range(n_cols):
                up_left = math.inf if c == 0 else matrix[r - 1][c - 1]
                up = matrix[r - 1][c]
                up_right = math.inf if c == n_cols - 1 else matrix[r - 1][c + 1]

                matrix[r][c] += min(up_left, up, up_right)

        return min(matrix[n_rows - 1])

    # Time Complexity: O(n * m)
    # Space Complexity: O(n)
    # Bottom Up Approach
    # REFERENCE: https://leetcode.com/problems/minimum-falling-path-sum/discuss/1634409/Top-down-and-bottom-up-DP-solutions-in-Python
    def minFallingPathSumDPList(self, matrix: List[List[int]]) -> int:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        import math
        dp_prev_row = matrix[n_rows - 1]

        for r in range(n_rows - 2, -1, -1):
            dp_curr_row = dp_prev_row.copy()

            for c in range(n_cols):
                bottom_left = math.inf if c == 0 else dp_prev_row[c - 1]
                bottom = dp_prev_row[c]
                bottom_right = math.inf if c == n_cols - 1 else dp_prev_row[c + 1]

                dp_curr_row[c] = matrix[r][c] + min(bottom_left, bottom, bottom_right)

            dp_prev_row = dp_curr_row

        return min(dp_prev_row)

    # Time Complexity: O(n * m)
    # Space Complexity: O(n)
    # Bottom Up Approach, add infinity padding before first and last columns
    # REFERENCE: https://leetcode.com/problems/minimum-falling-path-sum/discuss/1634409/Top-down-and-bottom-up-DP-solutions-in-Python
    def minFallingPathSumDPListWithPadding(self, matrix: List[List[int]]) -> int:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        import math
        dp_prev_row = [math.inf] + matrix[n_rows - 1] + [math.inf]

        for r in range(n_rows - 2, -1, -1):
            dp_curr_row = dp_prev_row.copy()

            for c in range(n_cols):
                dp_curr_row[c + 1] = matrix[r][c] + min(dp_prev_row[c], dp_prev_row[c + 1], dp_prev_row[c + 2])

            dp_prev_row = dp_curr_row

        return min(dp_prev_row)