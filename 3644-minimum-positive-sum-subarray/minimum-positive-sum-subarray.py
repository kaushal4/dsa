class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        pre = [nums[0]] 
        for i in range(1, len(nums)):
            pre.append(nums[i] + pre[-1])
        sol = -1
        print(pre)

        for i in range(l, r+1):
            low = 0
            high = i - 1 
            while high < len(nums):
                summ = pre[high] - pre[low] + nums[low]
                if summ > 0:
                    sol = min(sol, summ) if sol != -1 else summ
                high += 1
                low += 1

        return sol