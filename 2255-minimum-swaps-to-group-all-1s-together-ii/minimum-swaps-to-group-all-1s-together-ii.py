class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count_one = sum(nums)

        for i in range(count_one):
            nums.append(nums[i])
        size = len(nums)
        
        low = 0
        high = count_one - 1
        sub_count = sum(nums[low: high + 1])
        sol = (count_one - sub_count)
        while high < size:
            sol = min(count_one - sub_count, sol)
            high += 1
            if high < size: sub_count = sub_count + nums[high]
            if low < size: sub_count -= nums[low]
            low += 1 
        return sol