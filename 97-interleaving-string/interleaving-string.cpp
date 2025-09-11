class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int n = s1.size();
        int m = s2.size();
        int k = s3.size();
        if(n+m != k) return false;
        vector<vector<bool>> dp(n+1, vector<bool>(m+1, false));
        dp[0][0] = true;

        for(int i = 1; i < n+1; i++){
            if(s1[i-1] == s3[i-1] && dp[i-1][0]) dp[i][0] = true;
        }
        for(int i = 1; i < m+1; i++){
            if(s2[i-1] == s3[i-1] && dp[0][i-1]) dp[0][i] = true;
        }

        for(int i = 1; i < n+1; i++){
            for(int j = 1; j < m+1; j++){
                if(dp[i-1][j] && s1[i-1] == s3[i+j-1]) dp[i][j] = true;
                if(dp[i][j-1] && s2[j-1] == s3[i+j-1]) dp[i][j] = true;
            }
        }
        return dp[n][m];
    }
};