class Solution:
    def getDp(self, dp, i, j):
        if i > j:
            return 0
        return dp[i][j]

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(0,n):
            dp[i][i] = 1

        for a in range(1, n):
            j = a
            i = 0
            while( j < n ):
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], 2 + dp[i+1][j-1])
                dp[i][j] = max(dp[i][j], dp[i+1][j])
                dp[i][j] = max(dp[i][j], dp[i][j-1])
                i += 1
                j += 1

        return dp[0][n-1]