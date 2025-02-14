class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        high = 0
        low = 0
        sol = 0
        cur_sum = nums[high]
        window = {nums[high]}

        if len(window) == k:
            sol = max(sol, cur_sum)

        while(high < n-1):
            if nums[high+1] in window or len(window) == k:
                window.remove(nums[low])
                cur_sum -= nums[low]
                low += 1
            else:
                high += 1
                window.add(nums[high])
                cur_sum += nums[high]

            if len(window) == k:
                sol = max(sol, cur_sum)
        
        
        return sol