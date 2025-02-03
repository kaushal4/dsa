class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for j in range(n-1, 0, -1):
            for i in range(0,j):
                nums[i] = (nums[i] + nums[i+1]) % 10
        return nums[0]