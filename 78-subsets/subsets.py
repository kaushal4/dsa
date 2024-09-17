class Solution:
    def __init__(self):
        self.sol = []

    def recur(self, index, subset, nums: List[int]):
        if index >= len(nums):
            self.sol.append(subset)
            return
        option1 = subset.copy()
        option2 = subset.copy()
        option2.append(nums[index])
        self.recur(index+1, option1, nums)
        self.recur(index+1, option2, nums)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.recur(0, [], nums)
        return self.sol
        