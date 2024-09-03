class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        sol = list()
        
        for first in range(0, n-2):
            # condition - 1 to avoid duplicates
            if first > 0 and nums[first] == nums[first-1]:
                continue
            second = first + 1
            third = n - 1

            while (second < third):
                sum = nums[first] + nums[second] + nums[third]
                if sum == 0:
                    sol.append((nums[first], nums[second], nums[third]))
                    cur_second = second
                    cur_third = third
                    # condition - 2 to avoid duplicates
                    while second < n-1 and nums[cur_second] == nums[second]:
                        second += 1
                    # condition - 2 to avoid duplicates
                    while third > second and nums[cur_third] == nums[third]:
                        third -= 1
                elif (sum < 0):
                    second += 1
                else:
                    third -= 1
        return sol