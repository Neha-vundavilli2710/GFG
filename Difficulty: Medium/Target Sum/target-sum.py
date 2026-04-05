class Solution:
    def totalWays(self, arr, target):   # ✅ renamed
        
        total = sum(arr)
        
        # invalid cases
        if total + target < 0 or (total + target) % 2 != 0:
            return 0
        
        s1 = (total + target) // 2
        
        dp = [0] * (s1 + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(s1, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[s1]