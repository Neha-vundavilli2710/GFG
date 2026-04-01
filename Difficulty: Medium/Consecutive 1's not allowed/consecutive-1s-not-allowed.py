class Solution:
    def countStrings(self, n):
        
        if n == 1:
            return 2
        
        # dp[i-1]
        prev0 = 1  # ends with 0
        prev1 = 1  # ends with 1
        
        for _ in range(2, n + 1):
            curr0 = prev0 + prev1
            curr1 = prev0
            
            prev0 = curr0
            prev1 = curr1
        
        return prev0 + prev1