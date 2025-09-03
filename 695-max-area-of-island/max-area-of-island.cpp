class Solution {
public:
    bool check_valid(vector<vector<int>>& grid, vector<vector<bool>>& visited, int x, int y) { 
        int n = grid.size();
        int m = grid[0].size();
        if(x < 0 || x >= n || y < 0 || y >= m) return false;
        if(grid[x][y] == 0) return false;
        if(visited[x][y]) return false;
        return true;
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<bool>> visited(n, vector<bool> (m, false));
        int ans = 0;
        for(int i = 0; i< n; i++){
            for(int j = 0; j < m; j++){
                if(check_valid(grid, visited, i, j)){
                    ans = max(ans, dfs(grid, visited, i, j));
                }
            }
        }
        return ans;
    }

    int dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int x, int y){
        visited[x][y] = true;
        int size = 1;
        vector<pair<int, int>> directions({{1, 0}, {-1, 0}, {0, 1}, {0, -1}});
        for(auto& dir: directions){
            int new_x = x + dir.first;
            int new_y = y + dir.second;
            if(check_valid(grid, visited, new_x, new_y)){
                size += dfs(grid, visited, new_x, new_y);
            }
        }
        return size;
    }
};