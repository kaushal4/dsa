class Solution:
    def findItinerary(self, tickets):
        from collections import defaultdict
        import heapq

        # Step 1: Build the adjacency list (use a min-heap to maintain lexical order)
        adj = defaultdict(list)
        for start, end in tickets:
            heapq.heappush(adj[start], end)

        # Step 2: Perform Hierholzer's Algorithm
        itinerary = []

        def dfs(node):
            # Visit all edges from the current node
            while adj[node]:
                next_node = heapq.heappop(adj[node])
                dfs(next_node)
            # Append the node to the itinerary in reverse order
            itinerary.append(node)

        # Start DFS from "JFK"
        dfs("JFK")
        
        # Reverse the itinerary to get the correct order
        return itinerary[::-1]