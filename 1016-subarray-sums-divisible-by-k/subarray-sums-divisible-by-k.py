class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hash = dict()
        hash[0] = 1
        sum = 0
        sol = 0
        for num in nums:
            sum += num
            mod = sum % k

            if mod in hash:
                sol += hash[mod]
                hash[mod]+= 1
            else:
                hash[mod] = 1


        return sol