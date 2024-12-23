class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        freq = [0] * n
        for query in queries:
            freq[query[0]] += 1
            if query[1] < n-1:
                freq[query[1] + 1] -= 1
        
        cur_freq = 0
        for i in range(n):
            cur_freq += freq[i]
            if cur_freq < nums[i]:
                return False
        return True