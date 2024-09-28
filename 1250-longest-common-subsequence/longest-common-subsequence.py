class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0]*(n+2) for _ in range(m+2)]
        for i in range(n+2):
            dp[0][i] = 0
        for i in range(m+2):
            dp[i][0] = 0
        for i in range(1, m+2):
            for j in range(1, n+2):
                score = (dp[i-1][j-1] + 1) if ((i!=1 and j!=1) and text2[i-2] == text1[j-2]) else dp[i-1][j-1]
                dp[i][j] = max(max(dp[i-1][j],dp[i][j-1]),score)
        print(dp)
        return dp[m+1][n+1]

                

        