class Solution {
public:
    int minSizeSubarray(vector<int>& nums, int target) {
        int n = nums.size();
        int low = -1;
        long long high = -1;
        long long cur_sum = 0;
        long long base_sum = accumulate(nums.begin(), nums.end(),(long long) 0);
        long long sol = __LONG_LONG_MAX__;

        if(base_sum < target){
            high += int(target/base_sum) * n;
            cur_sum += int(target/base_sum) * base_sum;
        }

        while(low < n){
            if(cur_sum < target){
                if(cur_sum + base_sum <= target){
                    cur_sum += base_sum;
                    high += n; 
                } else {
                    high += 1;
                    cur_sum += nums[high%n];
                }
            } else {
                if(low != -1){
                    cur_sum -= nums[low];
                }
                low += 1;
            }
            if(cur_sum == target){
                if(low == -1){
                    sol = min(sol, (long long)high - low);
                } else {
                    sol = min(sol, (long long)high - low + 1);
                }
            }
        }
        return sol == INT_MAX?-1:sol;
    }
};