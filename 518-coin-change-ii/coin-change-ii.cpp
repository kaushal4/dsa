class Solution {
public:
    int change(int amount, vector<int>& coins) {
        if (amount == 0) return 1;
        if (coins.empty()) return 0;
        
        // Early impossibility detection based on parity
        bool hasOdd = false;
        for (int coin : coins) {
            if (coin > 0 && coin % 2 == 1) {
                hasOdd = true;
                break;
            }
        }
        
        // If amount is odd but all valid coins are even, impossible
        if (amount % 2 == 1 && !hasOdd) {
            return 0;
        }
        
        vector<int> dp(amount + 1, 0);
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