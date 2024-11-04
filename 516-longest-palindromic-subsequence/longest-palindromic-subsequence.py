class Solution:
    def getDp(self, dp, i, j):
        if i > j:
            return 0
        return dp[i][j]

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for a in range(0, n):
            j = a
            i = 0
            while( j < n ):
                if s[i] == s[j]:
                    score = 1 if i == j else 2
                    if dp[i][j] < (score + self.getDp(dp, i+1, j-1)):
                        dp[i][j] = score + self.getDp(dp, i+1, j-1)

                if dp[i][j] < self.getDp(dp, i+1, j):
                    dp[i][j] = max(dp[i][j], self.getDp(dp, i+1, j))
                if dp[i][j] < self.getDp(dp, i, j - 1):
                    dp[i][j] = max(dp[i][j], self.getDp(dp, i, j-1))
                i += 1
                j += 1
        return dp[0][n-1]