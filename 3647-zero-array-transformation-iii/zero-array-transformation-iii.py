class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        
        queries.sort()
        j = 0
        i = 0
        included = []
        excluded = []

        while(i < n):
            while j < m and queries[j][0] <= i:
                heapq.heappush(excluded, -queries[j][1])
                j+= 1
            while included and included[0] < i:
                heapq.heappop(included)
            while nums[i] > len(included):
                if (not excluded) or (-excluded[0]) < i:
                    return -1
                heapq.heappush(included, - heapq.heappop(excluded))
            i+= 1
            
        return len(excluded)