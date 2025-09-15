class Solution {
public:
    void printDp(vector<vector<bool>>& dp){
        int n = dp.size();
        int m = dp[0].size();
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                cout<<dp[i][j]<<" ";
            }
            cout<<endl;
        }
    }

    bool isMatch(string s, string p)
    {
        int n = p.size();
        int m = s.size();
        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
        dp[0][0] = true;
        for(int i = 1; i <= n; i++){
            if(p[i-1] == '*') dp[i][0] = dp[i-2][0];
        }
        for (int j = 1; j <= m; j++)
        {
            for (int i = 1; i <= n; i++)
            {
                if (p[i - 1] == '.' || p[i - 1] == s[j - 1])
                {
                    dp[i][j] = dp[i][j] || dp[i - 1][j - 1];
                }
                if (p[i - 1] == '*')
                {
                    dp[i][j] = dp[i][j] || dp[i - 2][j];
                    if (p[i - 2] == s[j - 1] || p[i - 2] == '.')
                    {
                        dp[i][j] = dp[i][j] || dp[i][j - 1];
                    }
                }
            }
        }
        //printDp(dp);
        return dp[n][m];
    }
};