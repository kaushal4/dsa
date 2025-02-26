class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state:
        # 1 = buying
        # 2 = selling
        # 3 = cooling down
        n = len(prices)
        @cache
        def recur(index:int, state:int) -> int:
            if index == n:
                return 0
            if state == 1:
                sol = 0
                sol = max(sol, - prices[index] + recur(index + 1, 2), recur(index + 1, 1))
                return sol
            if state == 2:
                sol = 0
                sol = max(sol,prices[index] + recur(index+1, 3), recur(index+1, 2))
                return sol
            return recur(index+1, 1)
        return recur(0, 1)