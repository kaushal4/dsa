class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [-1] * n
        dp[src] = 0

        adj = {c:[] for c in range(n)}

        for (fro, to, weight) in flights:
            adj[fro].append((to, weight))

        for _ in range(k+1):
            dp1 = dp.copy()
            for i in range(n):
                if dp[i] != -1:
                    for (child, weight) in adj[i]:
                        if dp1[child] == -1:
                            dp1[child] = dp[i] + weight
                        else:
                            dp1[child] = min(dp[i] + weight, dp1[child])
            dp = dp1
       
        return dp[dst]