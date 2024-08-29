class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [-1]*(amount + 1)
        mem[0] = 0
        for i in range(0, amount + 1):
            if mem[i] == -1:
                continue
            for coin in coins:
                if i + coin > amount:
                    continue

                if mem[i+coin] == -1:
                    mem[i+coin] = mem[i] + 1
                else:
                    mem[i+coin] = min(mem[i+coin], mem[i] + 1)
        return mem[amount]
        