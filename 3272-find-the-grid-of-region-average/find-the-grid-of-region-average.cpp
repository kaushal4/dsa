class Solution {
public:
    int score(vector<vector<int>>& image,int threshold, int x, int y){
        int sum = 0;
        for(int i = x; i <= x+2; i++){
            int prev = image[i][y];
            for(int j = y; j <= y+2; j++){
                if(abs(image[i][j] - prev) > threshold) return -1;
                sum += image[i][j];
                prev = image[i][j];
            }
        }
        for(int j = y; j <= y+2; j++){
            int prev = image[x][j];
            for(int i = x; i <= x+2; i++){
                if(abs(image[i][j] - prev) > threshold) return -1;
                prev = image[i][j];
            }
        }
        return (sum/9);
    }

    bool isValid(vector<vector<int>>& image, int x, int y){
        int n = image.size();
        int m = image[0].size();
        if(x < 0 || x >= n || y < 0 || y >= m) return false;
        return true;
    }

    int pointScore(vector<vector<int>>& image,unordered_map<int, int>& umap, int x, int y){
        int sum = 0;
        int validRegions = 0;
        for(int i = 0; i <= 2; i++){
            for (int j = 0; j <= 2; j++) {
                int r = x-i;
                int c = y-j;
                if(isValid(image, x - i, y - j) && umap.contains(r * 1000 + c) && umap[r * 1000 + c] > -1){
                    sum += umap[r * 1000 + c];
                    validRegions += 1;
                }
            }
        }
        if(validRegions == 0) return image[x][y];
        return (sum/validRegions);
    }

    vector<vector<int>> resultGrid(vector<vector<int>>& image, int threshold) {
        int n = image.size();
        int m = image[0].size();
        vector<vector<int>>ans (n, vector<int>(m, -1));
        unordered_map<int, int> umap;
        for(int i = 0; i < n-2 ;i++){
            for(int j = 0; j < m-2; j++){
                umap[i*1000 + j] = score(image, threshold, i, j);
            }
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                ans[i][j] = pointScore(image, umap, i, j);
            }
        }
        return ans;
    }
};