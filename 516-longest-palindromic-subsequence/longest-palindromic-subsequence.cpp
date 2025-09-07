class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();

        vector<vector<int>> dp (n+1, vector<int>(n+1, 0));

        for(int i = 1; i < n+1; i++){
            dp[i][i] = 1;
        }

        for(int i = n-1; i >= 1; i--){
            for(int j = i+1; j < n+1; j++) {
                dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
                if(s[i-1] == s[j-1]){
                    dp[i][j] = max(dp[i][j], 2 + dp[i+1][j-1]);
                }
            }
        }
        return dp[1][n];
    }
};