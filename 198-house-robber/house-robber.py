class Solution:
    def __init__(self) -> None:
        self.mem = []

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        self.mem = [-1] * n

        self.mem[0] = nums[0]
        if n == 1:
            return self.mem[0]
        self.mem[1] = nums[1]
        if n == 2:
            return max(self.mem[1], self.mem[0])
        self.mem[2] = nums[2] + self.mem[0]

        for i in range(3, n):
            self.mem[i] = nums[i] + max(self.mem[i-2], self.mem[i-3])

        return max(self.mem[n-2], self.mem[n-1])