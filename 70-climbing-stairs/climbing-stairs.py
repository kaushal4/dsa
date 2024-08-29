class Solution:

    def __init__(self) -> None:
        self.mem = [-1]

    def topDown(self, n) -> int:
        count = 0
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return 2
        if self.mem[n] != -1:
            return self.mem[n]
        count += self.topDown(n-1)
        count += self.topDown(n-2)

        self.mem[n] = count
        return count

    def climbStairs(self, n: int) -> int:
        self.mem = [-1] * n
        return self.topDown(n-1)