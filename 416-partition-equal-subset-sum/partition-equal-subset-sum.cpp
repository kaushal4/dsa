class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        if(n == 1) return false;
        int min_value = *min_element(nums.begin(), nums.end());
        int total_sum = accumulate(nums.begin(), nums.end(), 0);
        if(total_sum%2 != 0) return false;
        int desired_sum = total_sum/2;

        vector<bool> dp(desired_sum - min_value + 1, false);

        for (int j = 1; j < n + 1; j++)
        {
            for (int i = desired_sum; i >= min_value; i--)
            {
                if (i - nums[j - 1] < 0)
                    continue;
                if (i - nums[j - 1] == 0)
                    dp[i - min_value] = true;
                if (i - nums[j - 1] >= min_value)
                    dp[i - min_value] = (dp[i - min_value] || dp[i - nums[j - 1] - min_value]);
            }
        }

        return dp[desired_sum - min_value];
    }
};