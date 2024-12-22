class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        low = min(nums)
        nums = set(nums)
        if low < k:
            return -1
        if low == k:
            return len(nums) - 1
        return len(nums)
        