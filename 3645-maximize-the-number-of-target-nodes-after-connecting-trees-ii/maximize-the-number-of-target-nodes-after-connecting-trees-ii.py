class Solution:
    def createAdj(self, edges: List[List[int]]):
        adj = {i:[] for i in range(len(edges) + 1)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        return adj
    
    def dfs(self, adj: Dict[int, List[int]]):
        stack = [(0, 0)]
        visited = set()
        visited.add(0)
        coding = dict()
        a = 0
        b = 0
        while stack:
            node, code = stack.pop()
            if code % 2 == 0:
                a += 1
            else: b+= 1
            coding[node] = (code%2)
            for child in adj[node]:
                if not child in visited:
                    visited.add(child)
                    stack.append((child, code + 1))
        sol = []
        for i in range(len(adj.keys())):
            if coding[i] == 0:
                sol.append(a)
            else:
                sol.append(b)
        return sol


    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        adj1 = self.createAdj(edges1)
        adj2 = self.createAdj(edges2)
        l1 = self.dfs(adj1)
        l2 = self.dfs(adj2)
        b2 = max(l2)
        l1 = [i+b2 for i in l1]
        return l1