class Solution {
public:
    int get_height(vector<vector<int>>& heights, int x, int y) {
        int n = heights.size();
        int m = heights[0].size();
        if(x < 0 || x >= n|| y < 0 || y >= m) return -1;
        return heights[x][y];

    }

    bool is_valid(vector<vector<int>>& heights,vector<vector<bool>>& visited, int x, int y, int comp_height){
        int n = heights.size();
        int m = heights[0].size();
        if(x < 0 || x >= n|| y < 0 || y >= m) return false;
        if(visited[x][y]) return false;
        if(heights[x][y] < comp_height) return false;
        return true;
    }

    void bfs(vector<vector<int>>& heights, vector<vector<bool>>& visited, queue<pair<int, int>>& q){
        while(!q.empty()){
            pair<int, int> coords = q.front();q.pop();
            vector<pair<int, int>> directions({{1, 0}, {-1, 0}, {0, 1}, {0, -1}});
            for(const auto& dir: directions) {
                int new_x = coords.first + dir.first;
                int new_y = coords.second + dir.second;
                if(is_valid(heights, visited,new_x, new_y, get_height(heights, coords.first, coords.second))){
                    visited[new_x][new_y] = true;
                    q.push({new_x, new_y});
                }
            }
        }
    }
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int n = heights.size();
        int m = heights[0].size();
        vector<vector<bool>> atlantic(n, vector<bool>(m, false)), pacific(n, vector<bool> (m, false));
        queue<pair<int, int>> atlantic_q, pacific_q;
        for(int i = 0; i < n; i++){
            atlantic_q.push({i, -1});
            pacific_q.push({i, m});
        }
        for(int j = 0; j < m; j++){
            atlantic_q.push({-1, j});
            pacific_q.push({n, j});
        }
        bfs(heights, atlantic, atlantic_q);
        bfs(heights, pacific, pacific_q);
        vector<vector<int>> sol;
        for(int i = 0 ; i< n ; i++){
            for(int j = 0; j < m; j++){
                if(atlantic[i][j] && pacific[i][j]){
                    sol.push_back({i,j});
                }
            }
        }
        return sol;
    }
};