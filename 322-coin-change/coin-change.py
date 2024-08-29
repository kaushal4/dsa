class Solution:
    def __init__(self) -> None:
        self.mem = []

    def topDown(self, coins: List[int], amount: int):
        if amount == 0:
            return 0

        if self.mem[amount] != -2:
            return self.mem[amount]

        sol = sys.maxsize
        for c in coins:
            if amount - c >= 0:
                val = self.topDown(coins, amount - c)
                if val == -1:
                     continue
                sol = min(sol, 1 + self.topDown(coins, amount - c))
        self.mem[amount] = sol if sol != sys.maxsize else -1
        return self.mem[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.mem = [-2]*(amount + 1)
        return self.topDown(coins, amount)