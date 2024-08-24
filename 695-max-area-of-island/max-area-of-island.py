class Solution:
    def dfs(self, grid: List[List[str]], i: int, j:int, visited:Set[Tuple[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or (i,j) in visited or grid[i][j] == 0:
            return 0
        visited.add((i,j))
        score = 1
        score += self.dfs(grid, i+1, j, visited)
        score += self.dfs(grid, i, j+1, visited)
        score += self.dfs(grid, i-1, j, visited)
        score += self.dfs(grid, i, j-1, visited)
        return score


    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        visited:Set[Tuple[int]] = set()
        m = len(grid)
        n = len(grid[0])
        solution = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] != 0:
                    solution = max(self.dfs(grid, i, j, visited), solution)
        return solution