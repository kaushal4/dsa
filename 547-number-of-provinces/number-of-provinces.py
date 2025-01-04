class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        num_provences = 0
        visited = set()


        def dfs(node:int):
            if node in visited:
                return
            visited.add(node)
            for i in range(n):
                if isConnected[node][i]:
                    dfs(i)
        
        for i in range(n):
            if i not in visited:
                num_provences += 1
                dfs(i)
        
        return num_provences