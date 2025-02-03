class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        negative_count = 0
        count = 0
        n = len(nums)
        sol = 0

        for i in range(n):
            count += 1
            if nums[i] < 0: 
                negative_count += 1

            if nums[i] == 0:
                negative_count = 0
                count = 0
            
            if negative_count % 2 == 0:
                sol = max(sol, count)
        
        count= 0
        negative_count = 0
        
        for i in range(n-1, -1, -1):
            count += 1
            if nums[i] < 0: 
                negative_count += 1

            if nums[i] == 0:
                negative_count = 0
                count = 0
            
            if negative_count % 2 == 0:
                sol = max(sol, count)

        return sol