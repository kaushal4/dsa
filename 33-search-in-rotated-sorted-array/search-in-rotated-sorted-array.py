class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        low = 0 
        high = pivot 
        sol = -1

        while( low <= high):
            mid = low + (high - low)//2
            if (nums[mid] == target):
                sol = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if sol != -1:
            return sol

        low = pivot + 1
        high = len(nums) - 1

        while( low <= high):
            mid = low + (high - low)//2
            if (nums[mid] == target):
                sol = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return sol