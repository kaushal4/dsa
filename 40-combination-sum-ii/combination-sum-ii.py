class Solution:

    def recur(canditates, target, cur_sum, cur_arr, index):
        if cur_sum > target:
            return []
        if cur_sum == target:
            return [cur_arr.copy()]
        sol = []

        for i in range(index, len(canditates)):
            if i != index and canditates[i] == canditates[i-1]:
                continue

            cur_sum += canditates[i]
            cur_arr.append(canditates[i])
            recur_return = Solution.recur(canditates, target, cur_sum, cur_arr, i+1)
            cur_sum -= canditates[i]
            cur_arr.pop()
            if recur_return != None:
                sol = sol + recur_return
        
        return sol
            



    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return Solution.recur(candidates, target, 0, [], 0)

        