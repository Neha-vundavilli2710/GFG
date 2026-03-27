class Solution:
    def maxChocolate(self, grid):   # ✅ renamed
        
        n = len(grid)
        m = len(grid[0])
        
        dp = [[[0]*m for _ in range(m)] for _ in range(n)]
        
        # Base case
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    dp[n-1][j1][j2] = grid[n-1][j1]
                else:
                    dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        
        # Bottom-up DP
        for i in range(n-2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    
                    max_val = 0
                    
                    for dj1 in [-1, 0, 1]:
                        for dj2 in [-1, 0, 1]:
                            
                            nj1 = j1 + dj1
                            nj2 = j2 + dj2
                            
                            if 0 <= nj1 < m and 0 <= nj2 < m:
                                val = dp[i+1][nj1][nj2]
                                
                                if j1 == j2:
                                    val += grid[i][j1]
                                else:
                                    val += grid[i][j1] + grid[i][j2]
                                
                                max_val = max(max_val, val)
                    
                    dp[i][j1][j2] = max_val
        
        return dp[0][0][m-1]