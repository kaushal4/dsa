class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [amount + 1]*(amount + 1)
        mem[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >=0:
                    mem[i] = min(mem[i], mem[i - c] + 1)
        return mem[amount] if mem[amount] != (amount + 1) else -1
        