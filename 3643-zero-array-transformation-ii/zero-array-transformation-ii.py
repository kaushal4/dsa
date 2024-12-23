class Solution:
    def helper(self, nums: List[int], queries: List[List[int]], k:int):
        n = len(nums)
        freq = [0] * n
        for query in queries[:k]:
            freq[query[0]] += query[2]
            if query[1] < n-1:
                freq[query[1] + 1] -= query[2]
        
        cur_freq = 0
        for i in range(n):
            cur_freq += freq[i]
            if cur_freq < nums[i]:
                return False
        return True
    
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(queries)
        low = 0
        high = n
        sol = n+1
        while(low <= high):
            mid = low + (high - low)//2
            if(self.helper(nums, queries, mid)):
                sol = min(mid, sol)
                high = mid - 1
            else:
                low = mid + 1
        return sol if sol < n+1 else -1