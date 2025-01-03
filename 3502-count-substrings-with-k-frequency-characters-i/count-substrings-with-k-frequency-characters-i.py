class Solution:
    def printM(self, m):
        for i in m:
            for j in range(len(i)):
                print(i[j], end=" ")
            print()
        
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n)]
        if k == 1:
            dp[0][0] = 1
        
        for i in range(1, n):
            freq = {i:0 for i in range(26)}
            k_reached = False
            for j in range(i, -1, -1):
                c = ord(s[j]) - 97
                freq[c] += 1
                if freq[c] >= k: 
                    k_reached = True
                
                dp[i][j] = dp[i][j+1] + dp[i-1][j] - dp[i-1][j+1] + k_reached
        #self.printM(dp)
        
        return dp[n-1][0]