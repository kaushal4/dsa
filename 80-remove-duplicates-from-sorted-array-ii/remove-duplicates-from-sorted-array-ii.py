class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        low = 2
        high = 2

        while high < n:
            if nums[high] != nums[low-2]:
                nums[low] = nums[high]
                low += 1
            high += 1
        return low