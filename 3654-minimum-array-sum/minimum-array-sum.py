class Solution:
    def recur(self, nums: List[int], k: int, op1: int, op2: int, index: int, dp, done:List[bool] = (0, 0)):
        if index < 0:
            return 0
        if (index, op1, op2, done) in dp:
            return dp[(index, op1, op2, done)]
        best = nums[index] + self.recur(nums, k, op1, op2, index-1, dp)
        if op1 > 0 and not (done[0]):
            val = nums[index]
            nums[index] = math.ceil(val/2)
            best = min(best, self.recur(nums, k, op1 - 1, op2, index, dp, (1, done[1]))) 
            nums[index] = val
        if op2 > 0 and not (done[1]) and nums[index] >= k:
            val = nums[index]
            nums[index] = val - k
            best = min(best, self.recur(nums, k, op1, op2 - 1, index, dp, (done[0], 1))) 
            nums[index] = val
        dp[(index, op1, op2, done)] = best
        return best

    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        dp = {}
        return self.recur(nums, k, op1, op2, n-1, dp)