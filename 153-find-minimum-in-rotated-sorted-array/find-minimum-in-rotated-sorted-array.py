class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums) - 2
        pivot = high + 1
        while ( low <= high ):
            mid = low + (high - low) // 2
            if (nums[mid] > nums[mid + 1]):
                pivot = mid
                break
            elif nums[mid] > nums[pivot]:
                low = mid + 1
            else:
                high = mid - 1

        return nums[(pivot + 1) % len(nums)]