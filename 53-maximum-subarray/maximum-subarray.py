class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = nums[0]
        maxSum = nums[0]
        for num in nums[1:]:
            curMax = max(curMax, 0) + num
            maxSum = max(maxSum, curMax)
        return maxSum