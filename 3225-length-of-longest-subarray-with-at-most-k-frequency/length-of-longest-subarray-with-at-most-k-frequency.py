class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        heap = [] # (freq, index)
        high = 0
        low = 0
        n = len(nums)
        heapq.heappush(heap, (1, nums[0]))
        hash = {i:0 for i in nums}
        hash[nums[0]] = 1
        sol = 1

        while high+1 < n and low < n:
            if hash[nums[high + 1]] < k:
                high += 1
                hash[nums[high]] += 1
                sol = max(sol, high - low + 1)
            else:
                while hash[nums[high + 1]] == k:
                    hash[nums[low]] -= 1
                    low += 1
        return sol