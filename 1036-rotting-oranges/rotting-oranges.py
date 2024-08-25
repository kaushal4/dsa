class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited:Set[Tuple[int]] = set()

        queue:Deque[Tuple[int]] = deque()

        def addCell(i, j):
            if i < m and i >= 0 and j < n and j >= 0 and grid[i][j] != 0 and not (i,j) in visited:
                visited.add((i,j))
                grid[i][j] = 2
                queue.append((i,j))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    addCell(i,j)
        
        time:int = -1
        while queue:
            time += 1
            length = len(queue)
            for _ in range(length):
                (x, y) = queue.popleft()
                addCell(x+1, y)
                addCell(x, y+1)
                addCell(x, y-1)
                addCell(x-1, y)
        time = max(0, time)

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return time