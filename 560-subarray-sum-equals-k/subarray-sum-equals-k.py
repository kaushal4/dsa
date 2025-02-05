class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lookup:Dict[int, int] = defaultdict(lambda: 0)
        lookup[0] += 1
        count = 0
        correction = 0
        for i in range(n):
            rem = k - nums[i] - correction
            count += lookup[rem]

            correction += nums[i]
            lookup[-correction] += 1
        return count