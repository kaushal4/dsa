class Solution {
public:
    int change(int amount, vector<int>& coins) {
        using u128 = unsigned __int128;
        if (amount == 0) return 1;
        if (coins.empty()) return 0;
        
        vector<u128> dp(amount + 1, 0);
        dp[0] = 1;
        
        for (int coin : coins) {
            if (coin <= 0 || coin > amount) continue;
            
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i - coin];
            }
        }
        
        return dp[amount];
    }
};