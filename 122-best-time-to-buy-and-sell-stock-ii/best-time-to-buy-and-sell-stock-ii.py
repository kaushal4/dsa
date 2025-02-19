class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        base = prices[0]
        sell = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < sell:
                profit += sell - base
                sell = base = prices[i]
            else:
                sell = prices[i]
        if sell > base:
            profit += sell - base
        return profit