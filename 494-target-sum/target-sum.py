class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        agg = sum(nums)
        upper = agg
        lower = -agg        
        if target > upper or target < lower:
            return 0
        
        # check out the indexing
        dp = {}
        dp[0] = 1

        for i in range(0, len(nums)):
            dp_copy = {}
            for j in range(lower, upper + 1):
                if j - nums[i] >= lower:
                    if j-nums[i] in dp:
                        if j not in dp_copy:
                            dp_copy[j] = 0
                        dp_copy[j] += dp[j-nums[i]]
                if j + nums[i] <= upper:
                    if j+nums[i] in dp:
                        if j not in dp_copy:
                            dp_copy[j] = 0
                        dp_copy[j] += dp[j+nums[i]]
            dp = dp_copy
        return dp[target] if target in dp else 0