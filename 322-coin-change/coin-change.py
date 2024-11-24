class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for p in range(n):   
            coin = coins[p]
            for q in range(1, amount+1):
                if q - coin >= 0 and dp[q - coin] != -1:
                    dp[q] = min(dp[q], 1 + dp[q - coin]) if dp[q]!= -1 else 1 + dp[q - coin]
            #print(dp)
        return dp[amount]

                    
        