class Solution {
public:
    int numDistinct(string s, string t) {
        using u128 = __uint32_t;
        int n = s.size();
        int m = t.size();
        vector<vector<u128>> dp(n+1, vector<u128>(m+1, 0));
        for(int i = 0; i <= n;i++){
            dp[i][0] = 1;
        }

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(s[i-1] == t[j-1]) dp[i][j] += dp[i-1][j-1];
                dp[i][j] += dp[i-1][j];
            }
        }
        //print_dp(dp);

        return dp[n][m];
    }
};