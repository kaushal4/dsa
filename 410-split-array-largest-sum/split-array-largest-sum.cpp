class Solution {
public:
    bool checker(vector<int>& nums, int target, int k){
        int cur_sum = 0;
        int arr_count = 1;
        for(const auto& num: nums){
            if(cur_sum + num > target){
                cur_sum = num;
                arr_count += 1;
            } else {
                cur_sum += num;
            }
        }
        return arr_count <= k;
    }

    int splitArray(vector<int>& nums, int k) {
        int low = *max_element(nums.begin(), nums.end());
        int high = accumulate(nums.begin(), nums.end(), 0);
        int ans = -1;

        while(low <= high) {
            int mid = low + (high - low)/2;
            if(checker(nums, mid, k)){
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
};