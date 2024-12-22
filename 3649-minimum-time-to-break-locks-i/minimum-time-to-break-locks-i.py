class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        n = len(strength)
        @lru_cache(None)
        def r(mask, factor):
            if (mask == ((1 << n) - 1)):
                return 0
            best = float("inf")
            for i in range(n):
                if (mask & (1 << i) == 0):
                    time = math.ceil(strength[i] / factor)
                    best = min(best, time + r(mask | (1 << i), factor + k))
            return best
        return r(0, 1)