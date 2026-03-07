class Solution:
    def noOfWays(self, m, n, x):
        dp = [[0]*(x+1) for _ in range(n+1)]
        dp[0][0] = 1  # 0 dice, sum 0
        
        for dice in range(1, n+1):
            for summ in range(1, x+1):
                for face in range(1, m+1):
                    if summ - face >= 0:
                        dp[dice][summ] += dp[dice-1][summ-face]
        
        return dp[n][x]