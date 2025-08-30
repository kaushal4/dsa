class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        int prev_2 = 0;
        int prev = nums[0];

        for(int i = 1;i < n; i++) {
            int temp = prev;
            prev = max(prev, prev_2 + nums[i]);
            prev_2 = temp;
        }

        return prev;
    }
};