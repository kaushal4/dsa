class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2) > len(word1):
            word1 , word2 = word2, word1
        n = len(word1)
        m = len(word2)
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        if(n == 0 or m ==0):
            return max(n,m)
        dp[0][0] = 0
        for i in range(m+1):
            for j in range(n+1):
                if (j < n) and dp[i][j+1] > dp[i][j] + 1:
                    dp[i][j+1] = dp[i][j] + 1
                score = dp[i][j] if ((j < n and i < m) and word1[j] == word2[i]) else dp[i][j] + 1
                if (j < n and i < m) and dp[i+1][j+1] > score:
                    dp[i+1][j + 1] = score
                if i < m and dp[i+1][j] > dp[i][j] + 1:
                    dp[i+1][j] = (dp[i][j] + 1)
        # print(dp)
        return dp[m][n]