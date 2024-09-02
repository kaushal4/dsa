class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suff = []
        prod = 1
        sol = []

        for num in nums:
            prod = prod * num
            pre.append(prod)

        prod = 1

        for num in nums[::-1]:
            prod = prod * num
            suff.append(prod)
        
        suff.reverse()

        for i in range(0, len(nums)):
            sol_ele = 1
            if i > 0:
                sol_ele = sol_ele * pre[i - 1]

            if i < len(nums) - 1:
                sol_ele = sol_ele * suff[i + 1]

            sol.append(sol_ele)

        return sol