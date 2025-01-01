class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        new_parents = [-1] * n
        sol = [-1] * n

        def createTree(arr:List[int]) -> Dict:
            adj = {i:[] for i in range(n)}
            for i in range(len(arr)):
                if arr[i] != -1:
                    adj[arr[i]].append(i)
            return adj

        def dfs(node,  adj, parents):
            if s[node] in parents and parents[s[node]]:
                new_parents[node] = parents[s[node]][-1]
            else:
                new_parents[node] = parent[node]
                parents[s[node]] = []
            parents[s[node]].append(node)
            for child in adj[node]:
                dfs(child, adj, parents)
            parents[s[node]].pop()
        
        def node_count(node, adj) -> int:
            count = 1
            for child in adj[node]:
                count += node_count(child, adj)
            sol[node] = count
            return count
        
        adj = createTree(parent)
        parents = {}
        dfs(0, adj, parents)

        new_adj = createTree(new_parents)
        node_count(0, new_adj)
        return sol