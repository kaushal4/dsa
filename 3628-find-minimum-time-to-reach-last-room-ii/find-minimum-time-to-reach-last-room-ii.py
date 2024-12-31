class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        heap = [(0, (0,0), False)]
        visited = set()
        sol = -1

        def getChildren(x,y):
            coor = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            sol = []
            for co in coor:
                if co[0] >= 0 and co[0] < n and co[1] >= 0 and co[1] < m and (co not in visited):
                    sol.append(co)
            return sol

        while heap:
            (dist, (x,y), p) = heapq.heappop(heap)
            if (x,y) in visited: continue
            if x == n-1 and y == m-1:
                sol = dist
            visited.add((x,y))
            for cx,cy in getChildren(x, y):
                heapq.heappush(heap, (max(dist+1 + p, moveTime[cx][cy] + 1 + p), (cx,cy), not p))
        
        return sol