class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        sol = list()
        visited = set()
        
        for first in range(0, n-2):
            second = first + 1
            third = n - 1

            while (second < third):
                sum = nums[first] + nums[second] + nums[third]
                if sum == 0:
                    sol.append((nums[first], nums[second], nums[third]))
                    second += 1
                elif (sum < 0):
                    second += 1
                else:
                    third -= 1

        

        return list(set(sol))