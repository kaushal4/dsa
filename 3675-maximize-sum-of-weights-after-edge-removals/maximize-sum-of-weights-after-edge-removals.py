class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        hash = {i:[] for i in range(n)}
        for edge in edges:
            hash[edge[0]].append((edge[1], edge[2]))  
            hash[edge[1]].append((edge[0], edge[2])) 
        
        def dfs(i, pre = -1):
            options = []
            ex_sum = 0
            for (child, weight) in hash[i]:
                if child == pre: continue
                (including, excluding) = dfs(child, i) 
                ex_sum += excluding
                options.append(max(0, weight + including - excluding))
            return (ex_sum + sum(heapq.nlargest(k-1, options)), ex_sum + sum(heapq.nlargest(k, options)))
        return dfs(0)[1]