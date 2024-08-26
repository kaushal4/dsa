class Solution:
    def __init__(self) -> None:
        self.visited:Set[int] = set()
        self.checked:Set[int] = set()
        self.loop:bool = False
    
    def dfs(self, adj:List[List[int]], node:int):
        if node in self.checked:
            return
        if node in self.visited:
            self.loop = True
            return

        self.visited.add(node)

        for child in adj[node]:
            self.dfs(adj, child)
        
        self.visited.remove(node)
        self.checked.add(node)

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj:List[List[int]] = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
        
        for i in range(numCourses):
            if not i in self.visited:
                self.dfs(adj, i)
                if self.loop:
                    return False
        
        return not self.loop