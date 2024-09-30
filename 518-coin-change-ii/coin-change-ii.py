class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]
        if amount == 0:
            return 1
        for i in range(n):
            for j in range(1, amount+1):
                if j == coins[i]:
                    dp[i][j] = 1
                elif j - coins[i] > 0:
                    dp[i][j] = dp[i][j-coins[i]]
                if i >= 1:
                    dp[i][j] += dp[i-1][j]
        return dp[n-1][amount]