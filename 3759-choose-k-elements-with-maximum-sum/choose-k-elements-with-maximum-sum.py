class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        index_arr = [i for i in range(n)]
        sorting_arr = zip(nums1, nums2, index_arr)
        sorting_arr = sorted(sorting_arr)
        nums1, nums2, index_arr = list(zip(*(sorting_arr)))

        heap = []
        cur_sum = 0
        cur_val = 0
        val_sum = 0

        sol_sorted = [0] * n
        for i in range(n):
            if nums1[i] == cur_val:
                sol_sorted[i] = val_sum
            else:
                sol_sorted[i] = cur_sum
                val_sum = cur_sum
                cur_val = nums1[i]

            if len(heap) < k:
                cur_sum += nums2[i]
                heapq.heappush(heap, nums2[i])
            elif heap[0] < nums2[i]:
                low = heapq.heappop(heap)
                cur_sum -= low
                heapq.heappush(heap, nums2[i])
                cur_sum += nums2[i]
        
        sol = [0] * n

        for i in range(n):
            sol[index_arr[i]] = sol_sorted[i]
        
        return sol