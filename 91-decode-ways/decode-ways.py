class Solution:
    def check(self, a, b):
        a = int(a)
        b = int(b)
        if a == 1:
            return True
        if a == 2 and (b in range(0,7)):
            return True
        return False

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        if n == 0:
            return 0
        if n == 1:
            if int(s[0]) == 0:
                return 0
            return 1

        dp[n-1] = 1 if int(s[n-1]) != 0 else 0
        if int(s[n-2]) == 0:
            dp[n-2] = 0
        else:
            dp[n-2] = 1 + dp[n-1] if self.check(s[n-2], s[n-1]) else dp[n-1]
        
        for i in range(n-3, -1, -1):
            if int(s[i]) == 0:
                dp[i] = 0
                continue
            dp[i] = dp[i+1]
            if self.check(s[i],s[i+1]):
                dp[i]+= dp[i+2]
        
        return dp[0]

        