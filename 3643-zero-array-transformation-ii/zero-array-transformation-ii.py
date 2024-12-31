class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        i = 0
        j = 0
        freqs = [0] * (n+1)
        freq = 0
        while(i < n):
            freq += freqs[i]
            while(freq < nums[i]):
                if j >= m:
                    return -1
                query = queries[j]
                if query[0] > i:
                    freqs[query[0]] += query[2]
                elif query[0] <=i and query[1] >=i:
                    freq += query[2]
                freqs[query[1] + 1] -= query[2]
                j+=1
            i+= 1
        return j if i == n else -1