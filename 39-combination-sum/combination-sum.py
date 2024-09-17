class Solution:
    def __init__(self):
        self.sol = []

    def recur(self, candidates: List[int], target: int, index, cur_sum, cur_sequence):
        if cur_sum == target:
            self.sol.append(cur_sequence)
            return
        if cur_sum > target:
            return
        if index >= len(candidates):
            return
        
        self.recur(candidates, target, index + 1, cur_sum, cur_sequence)
        new_sequence = cur_sequence.copy()
        new_sequence.append(candidates[index])
        new_sum = cur_sum + candidates[index]
        self.recur(candidates, target, index, new_sum, new_sequence)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.recur(candidates, target, 0, 0, [])
        return self.sol