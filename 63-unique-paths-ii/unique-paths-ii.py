class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]

        def dfs(x:int, y:int):
            if x < 0 or x >= m or y < 0 or y >= n: return 0
            if obstacleGrid[x][y] == 1: return 0
            if x == m-1 and y == n-1:
                return 1
            if dp[x][y] != -1: return dp[x][y]
            score = 0
            score += dfs(x+1, y)
            score += dfs(x, y+1)
            dp[x][y] = score
            return score
        
        return dfs(0,0)

        