class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        vector<int> smallest_num(n, INT_MIN);
        int smallest_now = nums[0];
        for(int i = 1; i < n; i++) {
            if(smallest_now < nums[i]){
                smallest_num[i] = smallest_now;
            } else {
                smallest_now = nums[i];
            }
        }
        set<int> numbers_seen;
        numbers_seen.insert(nums[n-1]);
        for(int i = n-2; i >= 0; i--){
            auto right_biggest_ptr = numbers_seen.lower_bound(nums[i]);
            if(right_biggest_ptr == numbers_seen.begin()) {
                numbers_seen.insert(nums[i]);
                continue;
            }
            auto prev_ptr = std::prev(right_biggest_ptr);
            if(smallest_num[i] != INT_MIN && smallest_num[i] < *prev_ptr) 
                return true;
            numbers_seen.insert(nums[i]);
        }
        return false;
    }
};