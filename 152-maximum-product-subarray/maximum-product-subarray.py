class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = 1
        max_prod = 1
        sol = float("-inf")
        n = len(nums)

        for i in range(0, n):
            temp_min_prod = min(min(nums[i] * min_prod, nums[i] * max_prod), 1)
            max_prod = max(nums[i] * min_prod, nums[i] * max_prod)
            sol = max(max_prod, sol)
            max_prod = max(max_prod, 1)
            min_prod = temp_min_prod
        
        return sol