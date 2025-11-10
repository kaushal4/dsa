class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        score = 0

        while(k):
            highest_num = - heapq.heappop(nums)
            score += highest_num
            new_num = math.ceil(highest_num/3)
            heapq.heappush(nums, - new_num)
            k -= 1
        return score