class Solution:
    def findChain(self, hash: Set[int], visited: Set[int], curNum:int):
        if(curNum in visited or not curNum in hash):
            return 0
        visited.add(curNum)
        sol = 1
        sol += self.findChain(hash, visited, curNum + 1)
        sol += self.findChain(hash, visited, curNum - 1)
        return sol

    def longestConsecutive(self, nums: List[int]) -> int:
        sol = 0
        hash = set(nums)
        visited = set()
        for num in nums:
            sol = max(sol, self.findChain(hash, visited, num))
        return sol