class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 0
        pos = 0
        while n:
            n = n >> 1
            ans = ans | (1<<pos)
            pos += 1
        return ans

