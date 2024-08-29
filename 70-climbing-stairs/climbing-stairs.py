class Solution:

    def __init__(self) -> None:
        self.mem = [-1]

    def climbStairs(self, n: int) -> int:
        self.mem = [-1] * n
        self.mem[0] = 1
        if n == 1:
            return 1
        self.mem[1] = 2
        for i in range(2, n):
            self.mem[i] = self.mem[i-1] + self.mem[i-2]
        return self.mem[n-1]