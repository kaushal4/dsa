class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        for index in range(len(nums)):
            if nums[index] == -1:
                continue
            if nums[index] == -1:
                return nums[index] 
            val = nums[index]
            nums[index] = -2
            while True:
                if nums[val] == -1:
                    return val
                elif nums[val] == -2:
                    nums[val] = -1
                    break
                else:
                    temp = nums[val]
                    nums[val] = -1
                    val = temp

        return 0
