class Solution:
    def countBSTs(self, arr):
        sorted_arr = sorted(arr)
        n = len(arr)
        result = []
        for x in arr:
            i = sorted_arr.index(x)
            left = i
            right = n - i - 1
            result.append(self.countBST(left) * self.countBST(right))
        return result

    def countBST(self, n):
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]
