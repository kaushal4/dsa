class Solution {
public:
    int is_valid(vector<vector<char>>& grid,set<pair<int, int>>& visited, int x, int y) {
        int n = grid.size();
        int m = grid[0].size();
        if(x < 0 || x >= n || y < 0 || y >= m) return false;
        if(grid[x][y] == '0') return false;
        if(visited.contains({x, y})) return false;
        return true;
    }

    void update_coords(set<pair<int, int>>& visited, queue<pair<int, int>>& q, int x, int y){
        visited.insert({x, y});
        q.push({x, y});
    }

    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        set<pair<int, int>> visited;
        int count = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(!visited.contains({i, j}) && grid[i][j] == '1'){
                    count += 1;
                    bfs(grid, visited, i, j);
                }
            }
        }
        return count;
    }

    void bfs(vector<vector<char>>& grid,set<pair<int, int>>& visited, const int x,const int y) {
        visited.insert({x, y});
        queue<pair<int, int>> q;
        q.push({x, y});

        while(!q.empty()){
            auto coords = q.front();q.pop();
            vector<int> move({-1,1});
            for(int change: move){
                if(is_valid(grid, visited, coords.first + change, coords.second)){
                    update_coords(visited, q, coords.first + change, coords.second);
                }
                if(is_valid(grid, visited, coords.first, coords.second + change)){
                    update_coords(visited, q, coords.first, coords.second + change);
                }
            }
        }
    }
};