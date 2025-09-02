class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        if(n == 1) return false;
        int min_value = *min_element(nums.begin(), nums.end());
        int total_sum = accumulate(nums.begin(), nums.end(), 0);
        if(total_sum%2 != 0) return false;
        int desired_sum = total_sum/2;

        vector<vector<bool>> dp(desired_sum - min_value + 1, vector<bool> (n+1, false));

        for (int j = 1; j < n + 1; j++)
        {
            for (int i = min_value; i <= desired_sum; i++)
            {
                dp[i - min_value][j] = dp[i - min_value][j] || dp[i - min_value][j - 1];
                if (i - nums[j - 1] < 0)
                    continue;
                if (i - nums[j - 1] == 0)
                    dp[i - min_value][j] = true;
                if (i - nums[j - 1] >= min_value)
                    dp[i - min_value][j] = (dp[i - min_value][j] || dp[i - nums[j - 1] - min_value][j - 1]);
            }
        }

        bool sol = false;
        for(int j = 0; j < n+1; j++) {
            sol = sol || dp[desired_sum-min_value][j];
        }
        return sol;
    }
};