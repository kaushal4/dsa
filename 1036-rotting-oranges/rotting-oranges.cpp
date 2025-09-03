class Solution {
public:

    bool is_valid(vector<vector<int>>& grid, int x, int y){
        int n = grid.size();
        int m = grid[0].size();
        if(x < 0 || x >= n || y < 0 || y >= m) return false;
        if(grid[x][y] == 0 || grid[x][y] == 2) return false;
        return true;
    }

    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        int n = grid.size();
        int m = grid[0].size();
        for(int i = 0; i < n;i++){
            for(int j = 0; j < m; j++) {
                if(grid[i][j] == 2) q.push({i, j});
            }
        }
        int time = -1;

        while(!q.empty()) {
            time += 1;
            int q_size = q.size();

            while(q_size--){
                pair<int, int> coords = q.front();q.pop();
                vector<pair<int, int>> directions({{0,1}, {0, -1}, {1, 0}, {-1, 0}});

                for(const auto& dir : directions){
                    int new_x = coords.first + dir.first;
                    int new_y = coords.second + dir.second;
                    if(is_valid(grid, new_x, new_y)){
                        grid[new_x][new_y] = 2;
                        q.push({new_x, new_y});
                    }
                }
            }
        }
        bool all_done = true;

        for(int i = 0; i < n;i++){
            for(int j = 0; j < m; j++) {
                if(grid[i][j] == 1){
                    all_done = false;
                    break;
                }
            }
            if(!all_done) break;
        }
        return all_done?max(time, 0):-1;
    }
};