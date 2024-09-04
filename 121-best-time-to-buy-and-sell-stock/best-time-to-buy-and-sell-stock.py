class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        high = 1
        n = len(prices)
        sol = 0

        while high < n:
            sol = max(sol, prices[high] - prices[low])
            if prices[high] < prices[low]:
                low = high
            
            high += 1
        
        return sol 