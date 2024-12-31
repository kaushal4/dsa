class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or n == 0:
            return 0
        inc = [1] * n
        dec = [1] * n
        score = 1
        sol = 1

        for i in range(1,n):
            if nums[i] > nums[i-1]:
                score += 1
                inc[i] = max(score, inc[i])
            else:
                score = 1
        
        score = 1

        for i in range(n-3,-1,-1):
            if nums[i+1] < nums[i+2]:
                score += 1
                dec[i] = max(score, dec[i])
            else:
                score = 1
        
        for i in range(n):
            left = inc[i]
            right = dec[i]
            score = min(left, right)
            sol = max(sol, score)
        
        return sol 