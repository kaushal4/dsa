class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0] * n
        dp2 = [0] * n
        sol = 0

        # Take care of size constraints (Special Case)
        if n <= 3:
            return max(nums)

        dp1[0] = nums[0]
        dp1[1] = nums[1]
        dp1[2] = nums[2] + dp1[0]
        sol = max([dp1[0],dp1[1],dp1[2]])

        for i in range(3, n-1):
            dp1[i] = nums[i] + max(dp1[i-2], dp1[i-3])
            sol = max(dp1[i], sol)

        dp2[1] = nums[1]
        dp2[2] = nums[2]
        dp2[3] = nums[3] + nums[1]
        sol = max([dp2[1],dp2[2],dp2[3],sol])

        for i in range(4, n):
            dp2[i] = nums[i] + max(dp2[i-2], dp2[i-3])
            sol = max(dp2[i], sol)
        return sol