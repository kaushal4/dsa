class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        vector<vector<int>> dp(n+1,vector<int>(3, -1));
        dp[1][0] = -prices[1-1];
        dp[1][1] = -1;
        dp[1][2] = 0;

        for(int i = 2; i <= n;i++) {
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i-1]);
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i-1]);
            dp[i][2] = max(dp[i-1][2], dp[i-1][1]);
        }

        return max(dp[n][1], dp[n][2]);
    }
};