class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        def has_three_zeroes():
            count = 0
            max_count = 0
            for num in nums:
                if num == 0:
                    count += 1
                else: count = 0
                max_count = max(count, max_count)
            if max_count > 2:
                return True
            return False

        def findRight(i:int):
            while i != (size -1) and nums[i] == nums[i+1]:
                i += 1
            return i

        def findLeft(i:int):
            while i != 0 and nums[i] == nums[i-1] and nums[i]:
                i -= 1
            return i
        
        left_anchor = 0
        ans: List[List[int]] = []
        while left_anchor < size-2:
            low = findRight(left_anchor)
            low = low if low != left_anchor else left_anchor + 1
            high = size - 1
            while(low < high):
                if nums[left_anchor] + nums[low] + nums[high] == 0:
                    ans.append([nums[left_anchor], nums[low], nums[high]])
                
                if nums[left_anchor] + nums[low] + nums[high] < 0:
                    low = findRight(low) + 1
                else:
                    high = findLeft(high) - 1
            left_anchor = findRight(left_anchor)+1
        
        if has_three_zeroes():
            ans.append([0,0,0])

        return ans