class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s) # x
        m = len(t) # y
        dp = [[0] * (m+1) for _ in range(n+1)]

        # initialize
        for i in range(0, n+1):
            dp[i][0] = 1
        for j in range(1, m+1):
            dp[0][j] = 0

        for x in range(1,n + 1):
            for y in range(1, m + 1):
                if s[x-1] == t[y-1]:
                    dp[x][y] += dp[x-1][y-1]
                dp[x][y] += dp[x-1][y]
        
        return dp[n][m]