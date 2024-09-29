class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cooldown = 0
        lowest_buy = - prices[0]
        no_buy = 0
        for i in range(1,n):
            cooldown_new = max(lowest_buy + prices[i], no_buy)
            lowest_buy_new = max(no_buy - prices[i], lowest_buy)
            no_buy = max(cooldown, no_buy)
            cooldown = cooldown_new
            lowest_buy = lowest_buy_new
        return max(cooldown, no_buy)
        