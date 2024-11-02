class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        agg = sum(nums)
        upper = agg
        lower = -agg        
        if target > upper or target < lower:
            return 0
        
        # check out the indexing
        dp = [0] * (upper - lower + 1)
        dp[0 + upper] = 1

        for i in range(0, len(nums)):
            dp_copy = [0] * (upper - lower + 1)
            for j in range(lower, upper + 1):
                if j - nums[i] >= lower:
                    dp_copy[j + upper] += dp[j-nums[i] + upper]
                if j + nums[i] <= upper:
                    dp_copy[j + upper] += dp[j+nums[i] + upper]
            dp = dp_copy
        print(dp)
        return 0 if dp[target + upper] == -1 else dp[target + upper]