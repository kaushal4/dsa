class Solution:
    def bfs(self, adj:Dict[int, List[int]], source:int, k:int) -> int:
        if k < 0:
            return 0
        queue:Deque[int] = deque()
        queue.append(source)
        visited = set()
        visited.add(source)
        sol = 1
        while k and queue:
            b = len(queue)
            while(b):
                node = queue.popleft()
                for child in adj[node]:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
                        sol += 1
                b-= 1
            k -= 1
        return sol

    def getDist(self, adj:Dict[int, List[int]], k:int) -> List[int]:
        sol = []
        for i in range(0, len(adj.keys())):
            val = self.bfs(adj, i, k)
            sol.append(val)
        return sol

    def createAdj(self, edges:List[List[int]]):
        n = len(edges)
        adj = {i:[] for i in range(n + 1)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        return adj

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        adj1 = self.createAdj(edges1)
        adj2 = self.createAdj(edges2)
        dist2 = self.getDist(adj2, k-1)
        dist1 = self.getDist(adj1, k)
        best = max(dist2)
        for i in range(len(dist1)):
            dist1[i] += best
        return dist1