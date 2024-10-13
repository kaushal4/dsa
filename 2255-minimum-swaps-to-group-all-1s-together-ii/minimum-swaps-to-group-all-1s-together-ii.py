class Solution:
    def maxArrayOf(self, nums, n):
        cur_sum = 0
        low = 0
        high = n - 1
        cur_sum = sum(nums[low: high + 1])
        max_sum = cur_sum
        while high < len(nums) - 1 and low < len(nums):
            cur_sum = cur_sum - nums[low] + nums[high + 1]
            high += 1
            low += 1
            max_sum = max(max_sum, cur_sum)
        return max_sum

    def minArrayOf(self, nums, n):
        cur_sum = 0
        low = 0
        high = n - 1
        cur_sum = sum(nums[low: high + 1])
        min_sum = cur_sum
        while high < len(nums) - 1:
            cur_sum = cur_sum - nums[low] + nums[high + 1]
            high += 1
            low += 1
            min_sum = min(min_sum, cur_sum)
        return min_sum


    def minSwaps(self, nums: List[int]) -> int:
        count_1 = 0
        for num in nums:
            if num == 1:
                count_1 += 1
        return min(count_1 - self.maxArrayOf(nums, count_1),self.minArrayOf(nums, len(nums) - count_1))