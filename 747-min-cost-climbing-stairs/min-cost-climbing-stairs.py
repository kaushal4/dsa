class Solution:
    def __init__(self) -> None:
        self.mem = []

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 1
        self.mem = [-1] * n
        
        if n < 2:
            return 0
        self.mem[0] = 0
        self.mem[1] = 0
        for i in range(2, n):
            self.mem[i] = min(cost[i-1] + self.mem[i-1],cost[i-2] + self.mem[i-2])

        return self.mem[n-1]