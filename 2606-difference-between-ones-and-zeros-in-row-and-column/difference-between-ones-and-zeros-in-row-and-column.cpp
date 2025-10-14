class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<int> rows(n,0);
        vector<int> columns(m,0);
        for(int i = 0; i < n; i++){
            int row_sum = 0;
            for(int j = 0; j < m; j++){
                row_sum += grid[i][j];
            }
            rows[i] = row_sum;
        }
        for(int j = 0; j < m; j++){
            int col_sum = 0;
            for(int i = 0; i < n; i++){
                col_sum += grid[i][j];
            }
            columns[j] = col_sum;
        }
        vector<vector<int>> diff(n, vector<int>(m, 0));
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                diff[i][j] = rows[i] - (m - rows[i]) + columns[j] - (n - columns[j]);
            }
        }
        return diff;
    }
};

// 2 