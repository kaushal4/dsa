class Solution:
    def recur(self, matrix: List[List[int]], x:int, y:int, dp:List[List[int]]):
        m = len(matrix) # x
        n = len(matrix[0]) # y

        if dp[x][y] != -1:
            return dp[x][y]

        best_path = 1

        to_check = [(x+1, y),(x, y+1),(x-1, y),(x , y-1)]

        for (x_new, y_new) in to_check:
            if (x_new) < 0 or x_new >= m or (y_new) < 0 or y_new >= n:
                continue
            if matrix[x_new][y_new] > matrix[x][y]:
                best_path = max(best_path, 1 + self.recur(matrix, x_new, y_new, dp))
        
        dp[x][y] = best_path

        return best_path

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix) # x
        n = len(matrix[0]) # y
        dp = [[-1] * n for _ in range(m)]
        best = 0

        for x in range(m):
            for y in range(n):
                best = max(best, self.recur(matrix, x, y, dp))
        
        return best