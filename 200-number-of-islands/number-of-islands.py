class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited:Set[Tuple[int]] = set()
        m = len(grid)
        n = len(grid[0])
        def dfs(x: int, y:int):
            if(x >= m or x < 0 or y >= n or y < 0 or ((x,y) in visited) or grid[x][y] == "0"):
                return
            visited.add((x,y))
            move = [(1,0), (-1,0), (0,1), (0,-1)]
            for (dx, dy) in move:
                child_x = x + dx
                child_y = y + dy
                dfs(child_x, child_y)

        solution = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == "1":
                    solution += 1
                    dfs(i, j)
        return solution