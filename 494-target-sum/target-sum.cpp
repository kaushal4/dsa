class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        int low = accumulate(nums.begin(), nums.end(), 0, [](int acc, int num){
            return acc - num;
        });
        int high = accumulate(nums.begin(), nums.end(), 0);
        vector<int> dp(high - low + 1, 0);

        if(target < low || target > high) return 0;

        dp[0 - low] = 1;

        for(int i = 1; i < n+1; i++){
            vector<int> new_dp(high - low + 1, 0);
            for(int amt = low; amt < high + 1; amt++){
                if(nums[i-1] + amt < high + 1) {
                    new_dp[amt - low] += dp[nums[i-1] + amt - low];
                }
                if(amt - nums[i-1] >= low) {
                    new_dp[amt - low] += dp[amt - nums[i-1] - low];
                }
            }
            dp = new_dp;
        }
        return dp[target-low];
        
    }
};