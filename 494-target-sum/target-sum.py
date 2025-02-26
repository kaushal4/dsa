class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def recur(i:int, amt: int):
            if (i == n and amt == target):
                return 1
            if i >= n:
                return 0
            count = 0
            count += recur(i+1, amt + nums[i])
            count += recur(i+1, amt - nums[i])
            return count
        return recur(0, 0)