class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # create adjacency list
        adj = defaultdict(lambda: [])
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited = set()

         # Do DFS
        def dfs(node: int, history: List[int], parent:int) -> (list[int], int):
            print(history)
            if node in visited:
                return (history,  node)
            visited.add(node)
            starting_node = -1
            history.append(node)
            for child in adj[node]:
                if child == parent: continue
                (sol, starting_node) = dfs(child, history, node)
                if starting_node != -1:
                    return (sol, starting_node)
            history.pop()
            return ([], -1)

        # trimmed history to where the loop node starts
        s = 1
        history, loop_start = dfs(s, [], -1)
        start_pos = 0
        for i in range(len(history)):
            if history[i] == loop_start:
                start_pos = i
                break
        history = history[start_pos:]
        
        loop_edges = set()
        for i in range(len(history)-1):
            loop_edges.add((history[i], history[i+1]))
            loop_edges.add((history[i+1], history[i]))
        loop_edges.add((history[0], history[-1]))
        loop_edges.add((history[-1], history[0]))
            
        for i in range(len(edges)-1, -1, -1):
            cur_edge = edges[i]
            if (cur_edge[0], cur_edge[1]) in loop_edges:
                return (cur_edge[0], cur_edge[1])
        return -1

