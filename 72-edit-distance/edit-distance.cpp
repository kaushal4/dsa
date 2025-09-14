class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();
        using u32 = __uint32_t;
        constexpr u32 u32m = __UINT32_MAX__;
        vector<vector<u32>> dp (n+1, vector<u32> (m+1, u32m));
        dp[0][0] = 0;
        for(int i = 1; i < m+1; i++){
            dp[0][i] = 1 + dp[0][i-1];
        }
        for(int i = 1; i < n+1; i++){
            dp[i][0] = 1 + dp[i-1][0];
        }

        for(int i = 1; i < n+1; i++) {
            for(int j = 1; j< m+1; j++) {
                if(word1[i-1] == word2[j-1]){
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]);
                }
                dp[i][j] = min(dp[i][j], 1 + dp[i-1][j-1]);
                dp[i][j] = min(dp[i][j], 1 + dp[i-1][j]);
                dp[i][j] = min(dp[i][j], 1 + dp[i][j-1]);
            }
        }
        return dp[n][m];
        
    }
};