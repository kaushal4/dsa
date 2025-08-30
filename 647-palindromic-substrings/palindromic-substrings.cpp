class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();

        vector<vector<bool>> dp(n, vector<bool> (n, true));
        int ans = n;

        for(int i = n-2; i >= 0; i--){
            for(int j = n-1; j>i ; j--){
                dp[i][j] = s[i] == s[j] && dp[i+1][j-1];
                if(dp[i][j]){
                    ans += 1;
                }
            }
        }
        return ans;
    }
};