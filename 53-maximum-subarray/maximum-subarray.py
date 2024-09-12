class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sol = 0
        n = len(nums)
        all_neg = True
        for i in nums:
            if i > 0:
                all_neg = False
        if all_neg:
            return max(nums)
        cur_sum = 0
        for i in range(0, n):
            cur_sum = cur_sum + nums[i]
            if cur_sum < 0:
                cur_sum = 0
            sol = max(cur_sum, sol)
        return sol