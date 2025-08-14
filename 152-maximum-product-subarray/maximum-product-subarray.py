class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]

        imax = max(nums[0], 1)
        imin =  min(nums[0], 1)

        for num in nums[1:]:
            ans = max([imax * num, imin * num, ans])

            old_imax = imax
            imax = max([imax * num, imin * num, 1])
            imin = min([old_imax * num, imin * num, 1])

        return ans