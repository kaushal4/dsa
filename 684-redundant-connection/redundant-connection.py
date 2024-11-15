class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for edge in edges:
            if edge[0] in adj:
                adj[edge[0]].append(edge[1])
            else:
                adj[edge[0]] = []
                adj[edge[0]].append(edge[1])
            if edge[1] in adj:
                adj[edge[1]].append(edge[0])
            else:
                adj[edge[1]] = []
                adj[edge[1]].append(edge[0])
        
        stack = []
        stack.append(1)
        parent = {}
        visited = set()
        parent[1] = -1
        cycle_end = -1
        cycle_start = -1
        found:bool = False

        while stack and not found:
            node = stack.pop()
            visited.add(node)
            if node in adj:
                for child in adj[node]:
                    if parent[node] == child:
                        continue
                    if child in visited:
                        cycle_start = node 
                        cycle_end = child
                        found = True
                        break
                    parent[child] = node
                    stack.append(child)
        cycle_edges = set()
        cycle_edges.add((cycle_start, cycle_end))
        cycle_edges.add((cycle_end, cycle_start))
        cur_node = cycle_start
        while(cur_node != cycle_end):
            cycle_edges.add((cur_node, parent[cur_node]))
            cycle_edges.add((parent[cur_node], cur_node))
            cur_node = parent[cur_node]
        
        for edge in edges[::-1]:
            if (edge[0], edge[1]) in cycle_edges:
                return edge
        
        return (-1,-1)