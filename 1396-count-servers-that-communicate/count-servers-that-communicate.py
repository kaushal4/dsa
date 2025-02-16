class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        comm_set = set()

        for i in range(m):
            vals = []
            for j in range(n):
                if grid[i][j] == 1:
                    vals.append((i,j))
            if len(vals) < 2: continue
            for val in vals:
                comm_set.add(val)
        
        for j in range(n):
            vals = []
            for i in range(m):
                if grid[i][j] == 1:
                    vals.append((i,j))
            if len(vals) < 2: continue
            for val in vals:
                comm_set.add(val)
        return len(comm_set)