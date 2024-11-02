class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        if(n + m != len(s3)):
            return False
        for i in range(0, m+1):
            for j in range(0, n+1):
                if i-1 >= 0 and s3[j+i - 1] == s2[i-1] and dp[j][i-1] == 1:
                    dp[j][i] = 1
                if j-1 >= 0 and s3[j+i - 1] == s1[j-1] and dp[j-1][i] == 1: 
                    dp[j][i] = 1
        return True if dp[n][m]==1 else False