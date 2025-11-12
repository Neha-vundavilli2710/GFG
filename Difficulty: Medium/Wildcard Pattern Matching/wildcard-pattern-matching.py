class Solution:
    def wildCard(self, txt: str, pat: str) -> bool:
        n = len(txt)
        m = len(pat)

        # dp[i][j] is True if txt[0...i-1] matches pat[0...j-1]
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # Base case: Empty text matches empty pattern
        dp[0][0] = True

        # Initialization for the first row (txt is empty)
        for j in range(1, m + 1):
            if pat[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                
                # Case 1: Current pattern char is '?' or matches the text char
                if pat[j - 1] == '?' or pat[j - 1] == txt[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                
                # Case 2: Current pattern char is '*'
                elif pat[j - 1] == '*':
                    # '*' matches empty sequence (dp[i][j-1]) OR
                    # '*' matches one or more characters (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[n][m]

# The calling code at the bottom of your script expects the class:
# if Solution().wildCard(string, pattern):
#    ...