class Solution:
    def __init__(self):
        self.sol = []
        self.freq = dict()

    def recur(self, nums, index, cur):
        if index >= len(nums):
            self.sol.append(cur.copy())
            return 
        
        # add current index
        for i in range(self.freq[nums[index]]):
            cur.append(nums[index])
            self.recur(nums, index+1, cur)
            
        for i in range(self.freq[nums[index]]):
            cur.pop()
        # skip current index
        self.recur(nums, index+1, cur)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        no_dupe = []
        for num in nums:
            if num in self.freq:
                self.freq[num] += 1
            else:
                self.freq[num] = 1
                no_dupe.append(num)
        self.recur(no_dupe, 0, [])
        return self.sol
        