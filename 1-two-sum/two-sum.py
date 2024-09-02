class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_hash = dict()
        for index, num in enumerate(nums):
            rem = target - num
            if rem in freq_hash:
                return [freq_hash[rem], index]

            freq_hash[num] = index
        
        return [0,0]