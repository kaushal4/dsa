class Solution:
    def partition(self, nums, k:int, start, end):
        #pivot = nums[start] if start == end else nums[random.randint(start, end)]
        pivot = nums[start] if start == end else nums[random.randint(start, end)]
        low_index = start
        high_index = end
        check = start
        while (check <= high_index):
            if nums[check] == pivot:
                check += 1
            elif nums[check] > pivot:
                nums[check] , nums[low_index] = nums[low_index], nums[check]
                low_index += 1
                check += 1
            else:
                nums[check] , nums[high_index] = nums[high_index], nums[check]
                high_index -= 1
        
        if (low_index <= k and high_index >=k):
            return pivot
        elif (low_index > k):
            return self.partition(nums, k, start, low_index-1)
        return self.partition(nums, k, high_index+1, end)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.partition(nums, k-1, 0, len(nums)-1)