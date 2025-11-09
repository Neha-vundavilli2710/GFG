class Solution:
    def chocolatePickup(self, mat):
        from functools import lru_cache
        n = len(mat)

        # If start or end are blocked, no path exists
        if mat[0][0] == -1 or mat[n-1][n-1] == -1:
            return 0

        @lru_cache(None)
        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2  # since r1 + c1 == r2 + c2 (same total steps)
            
            # Out of bounds or blocked cell
            if (r1 >= n or c1 >= n or r2 >= n or c2 >= n or 
                mat[r1][c1] == -1 or mat[r2][c2] == -1):
                return float('-inf')

            # Reached bottom-right cell
            if r1 == c1 == n - 1:
                return mat[r1][c1]

            # Collect chocolates (avoid double-counting)
            chocolates = mat[r1][c1]
            if (r1, c1) != (r2, c2):
                chocolates += mat[r2][c2]

            # Try all 4 combinations of moves
            best_next = max(
                dp(r1 + 1, c1, r2 + 1),  # both down
                dp(r1, c1 + 1, r2),      # right + down
                dp(r1 + 1, c1, r2),      # down + right
                dp(r1, c1 + 1, r2 + 1)   # both right
            )

            chocolates += best_next
            return chocolates

        result = dp(0, 0, 0)
        return max(0, result)
