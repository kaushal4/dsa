class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins)
        m = len(coins[0])
        dp = [[[float("-inf")] * 3 for _ in range(m+1)] for _ in range(n+1)]
        for k in range(3):
            dp[0][1][k] = 0
            dp[1][0][k] = 0

        for i in range(1,n+1):
            for j in range(1,m+1):
                for k in range(3):
                    for dx, dy in [(-1,0), (0, -1)]:
                        nx, ny = i + dx, j + dy
                        dp[i][j][k] = max(dp[nx][ny][k] + coins[i-1][j-1], dp[i][j][k])
                        if k > 0:
                            dp[i][j][k] = max(dp[nx][ny][k-1], dp[i][j][k])
        
        return int(dp[n][m][2])