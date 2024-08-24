class Solution:
    def dfs(self, grid: List[List[str]], i: int, j:int, visited:Set[Tuple[int]]):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or (i,j) in visited or grid[i][j] == "0":
            return
        visited.add((i,j))
        self.dfs(grid, i+1, j, visited)
        self.dfs(grid, i, j+1, visited)
        self.dfs(grid, i-1, j, visited)
        self.dfs(grid, i, j-1, visited)


    def numIslands(self, grid: List[List[str]]) -> int:
        visited:Set[Tuple[int]] = set()
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] != "0":
                    count += 1
                    self.dfs(grid, i, j, visited)
        return count