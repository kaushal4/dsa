class Solution:
    def getVal(self, nums:List[int], index:int) -> int:
        if index == -1:
            return 0
        return nums[index]

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        low = -1
        high = 0
        sol = n

        for i in range(0, n):
            nums[i] = nums[i] + self.getVal(nums, i -1)

        if nums[n-1] < target:
            return 0
        
        while high < n:
            subSum = self.getVal(nums, high) - self.getVal(nums, low)
            if subSum < target:
                high += 1
            else:
                sol = min(sol, high - low)
                low += 1
                if low == high:
                    return 1
        
        return sol