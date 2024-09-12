class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = i = 0
        while i<=max_pos and i < len(nums):
            max_pos = max(i+nums[i], max_pos)
            i += 1
        return max_pos >= (len(nums) - 1)
        