class Solution:
    def bs(self, nums: List[int], tot, find):
        low = 0
        high = len(nums) - 2
        outllier = -1
        while low <= high:
            mid = low + (high-low)//2
            new_tot = tot - nums[mid]
            if new_tot == find:
                outllier = nums[mid]
                low = mid + 1
            elif new_tot < find:
                high = mid - 1 
            else:
                low = mid + 1
        return outllier

    def getLargestOutlier(self, nums: List[int]) -> int:
        nums.sort()
        tot = sum(nums)
        n = len(nums)
        sol = float("-inf")
        for i in range(n-1, -1, -1):
            nums[i], nums[n-1] = nums[n-1], nums[i]
            outlier = self.bs(nums,tot - nums[n-1], nums[n-1])
            if outlier != -1:
                sol = max(sol, outlier)
        return sol