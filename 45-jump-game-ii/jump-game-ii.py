class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        farthest = 0
        level_end = 0
        sol = 0

        if n == 1:
            return 0


        for i in range(0, n):
            distance = i + nums[i]
            farthest = max(farthest, distance)
            if distance >= n-1:
                sol += 1
                return sol
            
            if i >= level_end:
                sol += 1
                level_end = farthest
            
        return sol 