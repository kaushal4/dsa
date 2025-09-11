class Solution {
public:
    bool isValid(vector<vector<int>>& matrix, int x, int y, int px, int py){
        int n = matrix.size();
        int m = matrix[0].size();
        if(x < 0 || x >= n || y < 0 || y >= m) return false;
        if(px != -1 && matrix[x][y] <= matrix[px][py]) return false;
        return true;

    }

    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();

        vector<vector<int>> dp(n, vector<int>(m, -1));
        int best_score = 0;

        for(int i = 0 ; i< n; i++){
            for(int j = 0; j < m; j++){
                if(dp[i][j] == -1) dfs(matrix, dp, i, j, -1, -1);
                best_score = max(best_score, dp[i][j]);
            }
        }

        return best_score;
    }

    int dfs(vector<vector<int>>& matrix, vector<vector<int>>& dp, int x, int y, int px, int py) {
        if(!isValid(matrix, x, y, px, py)) return 0;
        if(dp[x][y]!=-1) return dp[x][y];
        int best_direction = 0;

        vector<pair<int, int>> directions({{1,0}, {-1, 0}, {0, 1}, {0, -1}});
        for(const auto& dir: directions){
            int new_x = x + dir.first;
            int new_y = y + dir.second;
            if(new_x != px || new_y != py) {
                best_direction = max(best_direction, dfs(matrix, dp, new_x, new_y, x, y));
            }
        }
        dp[x][y] = best_direction+1;
        return dp[x][y];
    }
};