class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        dp[0][0] = 0
        dp[1][0] = - prices[0]
        dp[2][0] = 0
        for i in range(1,n):
            dp[0][i] = max(dp[1][i-1] + prices[i], dp[2][i-1])
            dp[1][i] = max(dp[2][i-1] - prices[i], dp[1][i-1])
            dp[2][i] = max(dp[0][i-1], dp[2][i-1])
        return max(dp[0][n-1], dp[2][n-1])
        