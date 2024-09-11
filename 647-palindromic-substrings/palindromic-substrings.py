class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        sol = n

        #odd
        dp = [True] * n
        for i in range(2,n,2):
            for j in range(i, n):
                if s[j] == s[j-i] and dp[j-i+1]:
                    dp[j-i] = True
                    sol+= 1
                else:
                    dp[j-i] = False
        
        #Even
        dp = [True] * n

        for i in range(1,n,2):
            for j in range(i, n):
                if s[j] == s[j-i] and dp[j-i+1]:
                    dp[j-i] = True
                    sol+= 1
                else:
                    dp[j-i] = False
        
        return sol