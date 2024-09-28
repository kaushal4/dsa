class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*m for _ in range(n)] # n rows and m columns
        for i in range(n):
            dp[i][0] = 1
        for i in range(m):
            dp[0][i] = 1
        for j in range(1, m):
            for i in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]
        