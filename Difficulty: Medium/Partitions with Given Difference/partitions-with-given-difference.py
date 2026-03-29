class Solution:
    def countPartitions(self, arr, diff):
        
        total = sum(arr)
        
        # Invalid case
        if (total + diff) % 2 != 0:
            return 0
        
        target = (total + diff) // 2
        
        n = len(arr)
        
        # dp[i] = number of ways to make sum i
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[target]